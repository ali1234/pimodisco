import asyncio
import datetime
import string
import pathlib
import inflection
import re
from collections import defaultdict, deque

class historybuffer(deque):
    def __init__(self):
        super().__init__(maxlen=3)

    def too_fast(self, message):
        self.append(message)
        if len(self) < self.maxlen:
            return False
        return (self[-1].timestamp - self[0].timestamp) < datetime.timedelta(seconds = self.maxlen)

history = defaultdict(historybuffer)
last_warning = datetime.datetime.now()


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

    msg_time = datetime.datetime.now()

    if history[str(message.author)].too_fast(message):
        await client.delete_message(message)

        if msg_time - last_warning > datetime.timedelta(seconds=5):
            bot_message = await client.send_message(message.channel,
                                                "{}, please do not send spam!".format(message.author.mention))
            last_warning = msg_time
            await asyncio.sleep(4)
            await client.delete_message(bot_message)

        return True


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