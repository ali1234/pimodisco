import asyncio
import time
import string
import pathlib
import inflection
import re
from collections import defaultdict

history = defaultdict(int)
last_warning = 0


class ProfanityFilter(object):
    def __init__(self):
        self.tx = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
        with (pathlib.Path(__file__).parent / 'data' / 'badwords.txt').open() as bw:
            self._bad_words = list(word.strip() for word in bw.readlines() if len(word.strip()) > 0 and word[0] != '#')
        regex = r'|'.join(r'{}'.format(word) for word in self._bad_words)
        self.regex = re.compile(regex, re.IGNORECASE)

    def censor(self, string):
        ascii = inflection.transliterate(string.translate(self.tx))
        return self.regex.sub('*', ascii)

    def is_profane(self, string):
        ascii = inflection.transliterate(string.translate(self.tx))
        return self.regex.search(ascii)


pf = ProfanityFilter()

async def filter(client, message):
    global last_warning
    global history

    msg_time = time.time()
    spam_limit = msg_time - 2

    if history[str(message.author)] >= spam_limit:
        await client.delete_message(message)
        if msg_time - last_warning > 5:
            bot_message = await client.send_message(message.channel,
                                                "{}, please do not send spam!".format(message.author.mention))
            last_warning = msg_time
            await asyncio.sleep(5)
            await client.delete_message(bot_message)

        return True

    history[str(message.author)] = msg_time

    # Profanity Filter
    if pf.is_profane(message.content):
        await client.delete_message(message)
        bot_message = await client.send_message(message.channel,
                                                "Please refrain from using profanity {}.".format(message.author.mention))
        await asyncio.sleep(5)
        await client.delete_message(bot_message)
        return True

    return False


if __name__ == '__main__':
    import sys
    with open(sys.argv[1]) as allwords:
        for line in allwords:
            if pf.is_profane(line):
                print(line.strip())