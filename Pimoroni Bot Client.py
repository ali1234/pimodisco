import discord
import random
import logging


# ---Setup (Background Stuff)---


logger = logging.getLogger('log')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

    
# ---Documentation---


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    author = message.author

    if message.content.startswith('?help'):
        await client.send_message(message.channel, """```
A good ol' Pimoroni Robot (Pirated, of course)

Please Note:

    Since this bot runs in Python, all commands including a "space" within a single argument must be enclosed in quotation marks "like so",
    All command words must be preceded with a "?" token,
    And all commands are case sensitive!

Basic Commands:

- ?help: Displays this help sheet.
- ?hello: Says hello! A great way to find out your four digit user code. Woohoo for justification!
- ?joined [name]: Gives the exact datetime a member joined the server.
- ?roll: Rolls a standard 6 sided die!

Restricted Commands (Non-Member Users):

- ?say #[channel] [message]: Allows a priveledged member to "speak" through the bot to a specified channel.

```""")


# ---None-priveleged Commands---


    #HELLO
    elif message.content.startswith('?hello'):
        await client.send_message(message.channel, "Greetings {}!".format(author))
        
    #GOODBYE
    elif message.content.startswith('?goodbye'):
        await client.send_message(message.channel, "Tata {}!".format(author))

        
    #JOINED
    elif message.content.startswith("?joined"):
        msg = message.content
        words = msg.split()
        words.remove("?joined")
        for word in words:
            date = discord.Member.joined_at
            await client.send_message(message.channel, "Sorry, this function is not yet complete!")

            
    #ROLE
    elif message.content.startswith("?roll"):
        roll = str(random.randint(1, 6))
        await client.send_message(message.channel, "{} rolled!".format(roll))

# ---Priveleged Commands---


    #SAY
    elif message.content.startswith("?say"):
        msg = message.content
        words = msg.split()
        words.remove("?say")
        for word in words:
            if word == "#general":
                chan = "general"
            elif word == "#support":
                chan = "support"
            elif word == "#bilgetank":
                chan = "bilgetank"
            elif word == "#swashbucklers":
                chan = "swashbucklers"
            elif word == "#bot-testing":
                chan = "bot-testing"
            else:
                sendmsg.append(word)

        await client.send_message(message.channel, "Sorry, this function is not yet complete!")


# ------------Final Run (Don't put code after this!)------------


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('token')

