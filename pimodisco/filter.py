import asyncio
import time
import string
from collections import defaultdict
from profanityfilter import ProfanityFilter

history = defaultdict(int)
last_warning = 0

pf = ProfanityFilter(extra_censor_list=['brexit', 'trump'])

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
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))  # map punctuation to space
    if pf.is_profane(message.content.translate(translator)):
        await client.delete_message(message)
        bot_message = await client.send_message(message.channel,
                                                "Please refrain from using profanity {}.".format(message.author.mention))
        await asyncio.sleep(5)
        await client.delete_message(bot_message)
        return True

    return False
