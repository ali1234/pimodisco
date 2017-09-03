import discord
import random
import string
import asyncio
import time


# ---Setup (Background Stuff)---


testtoken = "token"
token = "token"


generaltest = "347821796692852749"
secondchanneltest = "348568515764158466"
general = "344893194573578241"
support = "344893396051034122"
bilgetank = "345202213137678337"
swashbucklers = "345226685295362059"
bot_testing = "348184000894074880"
music = "349213338829586443"


client = discord.Client()

    
# ---Documentation---


version = "2.0.2"

changelog = """```
Version {} Changelog:

- Fixed the anti-spam filter. Again.
```""".format(version)

history = {}

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
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
            bot_message = await client.send_message(message.channel, "{}, please do not send spam!".format(author.mention))
            await asyncio.sleep(5)
            await client.delete_message(bot_message)
            message = None
            history[str(message.author)] = None
            
    
    # Profanity Filter
    
    filter = ("brexit", "trump", "anal", "anus", "arse", "ass", "ballsack", "balls", "bastard", "bitch", "biatch", "bloody", "blowjob",  "bollock", "bollok", "boner", "boob", "bugger", "bum", "butt", "buttplug", "clitoris", "cock", "coon", "crap", "cunt", "damn", "dick", "dildo", "dyke", "fag", "feck", "fellate", "fellatio", "felching", "fuck", "fudgepacker", "flange", "goddamn", "hell", "homo", "jerk", "jizz", "knobend", "labia", "lmao", "lmfao", "muff", "nigger", "nigga", "omg", "penis", "piss", "poop", "prick", "pube", "pussy", "queer", "scrotum", "sex", "shit", "sh1t", "slut", "smegma", "spunk", "tit", "tosser", "turd", "twat", "vagina", "wank", "whore", "wtf")
    for word in words:
        word = word.lower()
        table = str.maketrans({key: None for key in string.punctuation})
        word = word.translate(table) 
        
        if word in filter:
            await client.delete_message(message)
            bot_message = await client.send_message(message.channel, "Please refrain from using profanity {}.".format(author.mention))
            await asyncio.sleep(5)
            await client.delete_message(bot_message)
            
    # End of Filter
    
    if message.content.startswith('?help'):
        msg = message.content
        hwords = msg.split()
        hwords.remove("?help")
        if len(hwords) < 1:
            await client.send_message(message.channel, """```
Version {}
A good ol' Pimoroni Robot (Pirated, of course)

Please Note:

    Since this bot runs in Python, all commands including a "\space\" within a single argument must be enclosed in quotation marks \"like so\", unless they contain numbers,
    All command words must be preceded with a \"?\" token,
    And all commands are case sensitive! If in doubt, use lower case!

Basic Commands:

- ?help [command]: Displays this help sheet. Add a command in there to get more information specifically for it!
- ?hello: Says hello! A great way to find out your four digit user code. Woohoo for justification!
- ?goodbye: Does the opposite of hello. How suprising!
- ?version: States the bot's current version.
- ?roll: Rolls a standard 6 sided die!
- ?choose [option1] [option2]: Chooses between two options!
- ?add [number1] [number2]: Adds two numbers together!
- ?link [page]: Gives you a link to a Pimoroni page, be it Twitter, YouTube or even just the shop!
- ?version: Gives you the version number of the Pimoroni Bot currently running.
- ?code: Gives you a link to the GitHub page of Pimoroni Bot.

Restricted Commands (Non-Member Users):

- ?changelog: Allows a priveledged member to state the changelog through the \"#general\" channel.
- ?say [channel] [message]: Allows a priveledged member to \"speak\" through the bot to a specified channel.

The source code for the Pimoroni Bot can be found here: https://github.com/RaspberryPicardBox/Pimoroni-Discord-Bot

```""".format(version))
        for word in hwords:
            word = word.lower()
            if word == "help":
                await client.send_message(message.channel, """```
The \"help\" command:
usage - ?help [command]
[command] = any command listed within the \"?help\" screen. Use without a \"?\".
If no command is entered, a general help sheet is shown.
```""")
            elif word == "hello":
                await client.send_message(message.channel, """```
The \"?hello\" command:
usage - ?hello
Says hello back to you!
```""")
            elif word == "goodbye":
                await client.send_message(message.channel, """```
The \"?goodbye\" command:
usage - ?goodbye
Says goodbye to you!
```""")
            elif word == "version":
                await client.send_message(message.channel, """```
The \"?version\" command:
usage - ?version
Says the currently active version of the bot.
```""")
            elif word == "roll":
                await client.send_message(message.channel, """```
The \"?roll\" command:
usage - ?roll
Rolls a standard 6 sided die and says the resulting number!
```""")
            elif word == "choose":
                await client.send_message(message.channel, """```
The \"?choose\" command:
usage - ?choose
[option1] and [option2] = Anything that you can't decide between!
Pseudo-randomly chooses between two options.
```""")
            elif word == "add":
                await client.send_message(message.channel, """```
The \"?add\" command:
usage - ?add [number1] [number2]
[number1] and [number2] = Any number, including decimals!
```""")
            elif word == "link":
                await client.send_message(message.channel, """```
The \"?link\" command:
usage - ?link [page]
[page] = Any of the Pimoroni pages. Usable terms:
    - shop
    - learn
    - blog
    - forums
    - twitter
    - youtube
    - about
    
Provides a lovely link to any Pimoroni page! Great for quick changes between Pimoroni gatherings.
```""")
            elif word == "version":
                await client.send_message(message.channel, """```
The \"?version\" command:
usage - ?version   
Says the current version number of the running Pimoroni Bot.
This is most useful for people whom want to work on the code for the bot.
The source code can be found here: https://github.com/RaspberryPicardBox/Pimoroni-Discord-Bot
```""")
            elif word == "code":
                await client.send_message(message.channel, """```
The \"?code\" command:
usage - ?code   
Gives you a link to the Pimoroni Bot's GitHub page.
```""")
            elif word == "changelog":
                await client.send_message(message.channel, """```
The \"?changelog\" command:
This command is restricted! Normal @general users cannot use this.
usage - ?changelog
States the latest changelog in the \"#general\" channel.
This is a priveledged command to prevent spam.
```""")
            elif word == "say":
                await client.send_message(message.channel, """```
The \"?say\" command:
This command is restricted! Normal @general users cannot use this.
usage - ?say [channel] [message]
[channel] = Any channel that Pimoroni Bot is in. Do not include the hash (#) symbol in this!
[message] = The message you wish Pimoroni Bot to say. This does not have to be inclosed in quotation marks.
Says a desired message into a channel via Pimoroni Bot.
```""")
            else:
                await client.send_message(message.channel, "Unrecognised command!")
                

# ---None-priveleged Commands---


    #HELLO
    elif message.content.startswith('?hello'):
        await client.send_message(message.channel, "Greetings {}!".format(author.mention))
        
    #GOODBYE
    elif message.content.startswith('?goodbye'):
        await client.send_message(message.channel, "Tata {}!".format(author.mention))
        
    #VERSION
    elif message.content.startswith('?version'):
        await client.send_message(message.channel, "Version {}!".format(version))
            
    #ROLL
    elif message.content.startswith("?roll"):
        roll = str(random.randint(1, 6))
        await client.send_message(message.channel, "{} rolled!".format(roll))
        
    #CHOOSE
    elif message.content.startswith("?choose"):
        num = random.randint(1, 2)
        msg = message.content
        cwords = msg.split()
        cwords.remove("?choose")
        print(cwords)
        print(num)
        if num == 1:
            await client.send_message(message.channel, "Definitely {}".format(cwords[0]))
        elif num == 2:
            await client.send_message(message.channel, "Definitely {}".format(cwords[1]))
        
    
    #ADD
    elif message.content.startswith("?add"):
        msg = message.content
        awords = msg.split()
        awords.remove("?add")
        numbers = []
        for word in awords:
            try:
                float(word)
                numbers.append(word)
            except:
                await client.send_message(message.channel, "Your numbers weren't numbers!")
        answer = float(numbers[0]) + float(numbers[1])
        print(answer)
        await client.send_message(message.channel, "The answer is: {}".format(answer))
        
        
    #LINK
    elif message.content.startswith("?link"):
        msg = message.content
        lwords = msg.split()
        lwords.remove("?link")
        for word in lwords:
            word = word.lower()
            if word == "shop":
                await client.send_message(message.channel, "Here's a link to the Pimoroni shop: https://shop.pimoroni.com/")
            elif word == "learn":
                await client.send_message(message.channel, "Here's a link to the Pimoroni Yarr-niversity: https://learn.pimoroni.com/")
            elif word == "blog":
                await client.send_message(message.channel, "Here's a link to the Pimoroni blog: http://blog.pimoroni.com/")
            elif word == "forum" or word == "forums":
                await client.send_message(message.channel, "Here's a link to the Pimoroni forums: http://forums.pimoroni.com/")
            elif word == "twitter":
                await client.send_message(message.channel, "Here's a link to the Pimoroni Twitter: http://twitter.com/pimoroni")
            elif word == "youtube":
                await client.send_message(message.channel, "Here's a link to the Pimoroni YouTube channel: http://youtube.com/pimoroniltd")
            elif word == "about":
                await client.send_message(message.channel, "Here's a link to the Pimoroni \"about us\" page: https://shop.pimoroni.com/pages/about-us")
            else:
                await client.send_message(message.channel, "Unable to find Pimoroni related link!")
                
            
    #VERSION
    elif message.content.startswith("?version"):
        await client.send_message(message.channel, "Version: {}".format(version))
        
    
    #CODE
    elif message.content.startswith("?code"):
        await client.send_message(message.channel, "Here's a link: https://github.com/RaspberryPicardBox/Pimoroni-Discord-Bot")
                

# ---Priveleged Commands---


    #CHANGELOG
    elif message.content.startswith("?changelog"):
        if "@swashbucklers" in [y.name.lower() for y in author.roles] or "@staff" in [y.name.lower() for y in author.roles]:
            try:
                await client.send_message(discord.Object(generaltest), changelog)
            except:
                print("Not on test server!")
            try:
                await client.send_message(discord.Object(general), changelog)
            except:
                print("Not on real server!")
        else:
            await client.send_message(message.channel, "You do not have permission to use this command.")
        

    #SAY
    elif message.content.startswith("?say"):
        if "@swashbucklers" in [y.name.lower() for y in author.roles] or "@staff" in [y.name.lower() for y in author.roles]:
            msg = message.content
            swords = msg.split()
            swords.remove("?say")
            sendmsg = []
            chan = "channel"
            for word in swords:
                global chan
                if word == "generaltest":
                    chan = generaltest
                    pass
                elif word == "secondchanneltest":
                    chan = secondchanneltest
                    pass
                elif word == "general":
                    chan = general
                    pass
                elif word == "support":
                    chan = support
                    pass
                elif word == "bilgetank":
                    chan = bilgetank
                    pass
                elif word == "swashbucklers":
                    chan = swashbucklers
                    pass
                elif word == "bot-testing":
                    chan = bot_testing
                    pass
                elif word == "bot-testing":
                    chan = music
                    pass
                else:
                    sendmsg.append(word)
            sendmsgs = " ".join(sendmsg)
            await client.send_message(discord.Object(id=chan), "{}".format(str(sendmsgs)))
        else:
            await client.send_message(message.channel, "You do not have permission to use this command.")
            
            
#---Automatic Events---
            
    
@client.event
async def on_member_join(member):
    welcome = await client.send_message(discord.Object(general), "Welcome {} to the Officially Unofficial Pimoroni Discord Server!".format(member.mention))
    await asyncio.sleep(5)
    await client.delete_message(welcome)


# ------------Final Run (Don't put code after this!)------------


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    try:
        await client.send_message(discord.Object(bot_testing), "Pimoroni Bot started...")
    except:
        print("Not on real server!")
    try:
        await client.send_message(discord.Object(generaltest), "Pimoroni Bot started...")
    except:
        print("Not on test server!")
        

client.run(token)



