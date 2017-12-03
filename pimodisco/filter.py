import asyncio
import time
import string
from collections import defaultdict

history = defaultdict(int)

async def filter(client, message):
    msg_time = time.time()
    spam_limit = msg_time - 2

    words = message.content.split()

    if history[str(message.author)] >= spam_limit:
        await client.delete_message(message)
        bot_message = await client.send_message(message.channel,
                                                "{}, please do not send spam!".format(message.author.mention))
        await asyncio.sleep(5)
        await client.delete_message(bot_message)
        history[str(message.author)] = 0
        return True
    else:
        history[str(message.author)] = msg_time

    # Profanity Filter

    filter = (
    "brexit", "trump", "anal", "anus", "arse", "ass", "ballsack", "balls", "bastard", "bitch", "biatch", "bloody",
    "blowjob", "bollock", "bollok", "boner", "boob", "bugger", "bum", "butt", "buttplug", "clitoris", "cock", "coon",
    "crap", "cunt", "damn", "dick", "dildo", "dyke", "fag", "feck", "fellate", "fellatio", "felching", "fuck",
    "fudgepacker", "flange", "goddamn", "hell", "homo", "jerk", "jizz", "knobend", "labia", "lmao", "lmfao", "muff",
    "nigger", "nigga", "omg", "penis", "piss", "poop", "prick", "pube", "pussy", "queer", "scrotum", "sex", "shit",
    "sh1t", "slut", "smegma", "spunk", "tit", "tosser", "turd", "twat", "vagina", "wank", "whore", "wtf")
    for word in words:
        word = word.lower()
        table = str.maketrans({key: None for key in string.punctuation})
        word = word.translate(table)

        if word in filter:
            await client.delete_message(message)
            bot_message = await client.send_message(message.channel,
                                                    "Please refrain from using profanity {}.".format(message.author.mention))
            await asyncio.sleep(5)
            await client.delete_message(bot_message)
            return True

    return False
