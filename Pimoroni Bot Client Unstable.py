import discord
import random
import logging


# ---Setup (Background Stuff)---


logger = logging.getLogger('unstable')
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

    Since this bot runs in Python, all commands including a "space" within a single argument must be enclosed in quotation marks "like so", unless they contain numbers,
    All command words must be preceded with a "?" token,
    And all commands are case sensitive!

Basic Commands:

- ?help: Displays this help sheet.
- ?hello: Says hello! A great way to find out your four digit user code. Woohoo for justification!
- ?goodbye: Does the opposite of hello. How suprising!
- ?roll: Rolls a standard 6 sided die!
- ?add [number1] [number2]: Adds two numbers together!

Restricted Commands (Non-Member Users):

- ?say [channel] [message]: Allows a priveledged member to "speak" through the bot to a specified channel.

```""")


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
                if word == "general":
                    chan = "344893194573578241"
                    pass
                elif word == "support":
                    chan = "344893396051034122"
                    pass
                elif word == "bilgetank":
                    chan = "345202213137678337"
                    pass
                elif word == "swashbucklers":
                    chan = "345226685295362059"
                    pass
                elif word == "bot-testing":
                    chan = "348184000894074880"
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

client.run('token')


