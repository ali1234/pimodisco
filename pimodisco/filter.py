import asyncio
import time
import string

history = {}

async def filter(client, message):
    author = message.author

    msg_time = time.time()
    spam_limit = msg_time - 2

    msg = message.content
    channel = message.channel
    words = msg.split()

    history_item = history.get(str(message.author))
    history[str(message.author)] = msg_time
    print(history_item)
    print(msg_time)
    try:
        history_item = int(history_item)
    except:
        print("Nonetype in message history...")
    if history_item == None:
        print("Adding history event...")
        history[str(message.author)] = msg_time
    else:
        if history_item >= spam_limit:
            await client.delete_message(message)
            bot_message = await client.send_message(message.channel,
                                                    "{}, please do not send spam!".format(author.mention))
            await asyncio.sleep(5)
            await client.delete_message(bot_message)
            message = None
            history[str(message.author)] = None
            return True

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
                                                    "Please refrain from using profanity {}.".format(author.mention))
            await asyncio.sleep(5)
            await client.delete_message(bot_message)
            return True

    return False
