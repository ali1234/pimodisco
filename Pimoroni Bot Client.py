import discord
import random
import logging

import discord
import random
import logging

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


logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

    
# ---Documentation---


version = "1.3"

changelog = """```
Version {} Changelog:
- Removed the annoying changelog printing on reboot and opted for a manual send. Priveledged users can use \"?changelog\" in order to send the changelog to the \"#general\" tab.
- Added \"version\" command with the new implementation of version numbering. This command simply specifies the bot's version number. Most helpful for people wanting to work on current versions of the bot.
- Added the \"code\" command. This gives you a link to the GitHub page of Pimoroni Bot.
- Updated the \"say\" command to include the new \"#music\" channel.
- Added a new announcement for when the bot comes onlines (displaying in #bot-testing only).
```""".format(version)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    author = message.author

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
- ?roll: Rolls a standard 6 sided die!
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
            elif word == "roll":
                await client.send_message(message.channel, """```
The \"?roll\" command:
usage - ?roll
Rolls a standard 6 sided die and says the resulting number!
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
        await client.send_message(message.channel, "Greetings {}!".format(author))
        
    #GOODBYE
    elif message.content.startswith('?goodbye'):
        await client.send_message(message.channel, "Tata {}!".format(author))
            
    #ROLL
    elif message.content.startswith("?roll"):
        roll = str(random.randint(1, 6))
        await client.send_message(message.channel, "{} rolled!".format(roll))
        
    
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
    await client.send_message(general, "Welcome @{0} to the Officially Unofficial Pimoroni Discord Server!".format(member))


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


logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

    
# ---Documentation---


version = "1.1"

changelog = """```
Version {} Changelog:
- Improved the help documentation to allow for specific command help requests. Try \"?help link\"!
```""".format(version)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    author = message.author

    if message.content.startswith('?help'):
        msg = message.content
        hwords = msg.split()
        hwords.remove("?help")
        if len(hwords) < 1:
            await client.send_message(message.channel, """```
Version {}
A good ol' Pimoroni Robot (Pirated, of course)

Please Note:

    Since this bot runs in Python, all commands including a "space" within a single argument must be enclosed in quotation marks "like so", unless they contain numbers,
    All command words must be preceded with a "?" token,
    And all commands are case sensitive! If in doubt, use lower case!

Basic Commands:

- ?help [command]: Displays this help sheet. Add a command in there to get more information specifically for it!
- ?hello: Says hello! A great way to find out your four digit user code. Woohoo for justification!
- ?goodbye: Does the opposite of hello. How suprising!
- ?roll: Rolls a standard 6 sided die!
- ?add [number1] [number2]: Adds two numbers together!
- ?link [page]: Gives you a link to a Pimoroni page, be it Twitter, YouTube or even just the shop!

Restricted Commands (Non-Member Users):

- ?say [channel] [message]: Allows a priveledged member to "speak" through the bot to a specified channel.

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
            elif word == "roll":
                await client.send_message(message.channel, """```
The \"?roll\" command:
usage - ?roll
Rolls a standard 6 sided die and says the resulting number!
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
        await client.send_message(message.channel, "Greetings {}!".format(author))
        
    #GOODBYE
    elif message.content.startswith('?goodbye'):
        await client.send_message(message.channel, "Tata {}!".format(author))
            
    #ROLL
    elif message.content.startswith("?roll"):
        roll = str(random.randint(1, 6))
        await client.send_message(message.channel, "{} rolled!".format(roll))
        
    
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
                

# ---Priveleged Commands---


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
                else:
                    sendmsg.append(word)
            sendmsgs = " ".join(sendmsg)
            await client.send_message(discord.Object(id=chan), "{}".format(str(sendmsgs)))
        else:
            await client.send_message(message.channel, "You do not have permission to use this command.")
            
            
#---New Member---
            
    
@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))


# ------------Final Run (Don't put code after this!)------------


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    try:
        await client.send_message(discord.Object(generaltest), changelog)
    except:
        print("Not on test server!")
    try:
        await client.send_message(discord.Object(general), changelog)
    except:
        print("Not on real server!")
        

client.run(token)




