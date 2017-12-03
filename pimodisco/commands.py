import random

from pimodisco import version

commands = {}

def command(f):
    """Decorator to mark a function as a command."""
    commands[f.__name__] = f
    return f

def authorized(f):
    """Decorator to make a command as authorized."""
    async def checkauth(client, message):
        authorized_roles = ['@swashbucklers', '@staff']
        roles = [y.name.lower() for y in message.author.roles]
        if any(role in roles for role in authorized_roles):
            await f(client, message)
        else:
            await client.send_message(message.channel, "You do not have permission to use this command.")
    checkauth.__name__ = f.__name__
    checkauth.__doc__ = f.__doc__
    return checkauth


@command
async def help(client, message):
    """Prints help about commands. With no argument, prints general help."""
    words = message.content.split()
    if len(words) > 1:
        if words[1] in commands:
            f = commands[words[1]]
            await client.send_message(message.channel, '```{}```'.format(' '.join([f.__name__, f.__doc__])))
        else:
            await client.send_message(message.channel, "I don't know that command. Type !help for a list of commands.")
    else:
        await client.send_message(message.channel, """```A good ol' Pimoroni Robot (Pirated, of course)
Version {}

The source code for the Pimoroni Bot can be found here: https://github.com/RaspberryPicardBox/Pimoroni-Discord-Bot
        
Commands: {}

Type !help <command> for help with that command.```""".format(version,
            '\n'.join(' - {}: {}'.format(f.__name__, f.__doc__) for f in sorted(commands.values(), key = lambda f: f.__name__))
        ))

@command
async def hello(client, message):
    """Says hello back to you!"""
    greetings = ['Hello', 'Hi', 'Greetings', "What's up"]
    await client.send_message(message.channel, '{} {}!'.format(random.choice(greetings), message.author.mention))

@command
async def goodbye(client, message):
    """Says goodbye back to you!"""
    goodbyes = ['Goodbye', 'See you', 'Later', 'Tata']
    await client.send_message(message.channel, '{} {}!'.format(random.choice(goodbyes), message.author.mention))

@command
async def version(client, message):
    """Says the currently active version of the bot."""
    await client.send_message(message.channel, 'Version {}'.format(version))

@command
async def code(client, message):
    """Prints a link to the bots code."""
    await client.send_message(message.channel,
                  "Here's a link to my source code: https://github.com/RaspberryPicardBox/Pimoroni-Discord-Bot")

@command
async def roll(client, message):
    """Roll a six-sided die."""
    roll = str(random.randint(1, 6))
    await client.send_message(message.channel, '{} rolled!'.format(roll))

@command
async def choose(client, message):
    """Choose something from a list of options."""
    recommendations = ['Try', 'Go with', 'Maybe', 'Definitely', 'Consider', 'I asked @Gadgetoid and he said']
    cwords = message.content.split()[1:]
    if len(cwords) > 0:
        await client.send_message(message.channel, '{} {}.'.format(random.choice(recommendations), random.choice(cwords)))
    else:
        await client.send_message(message.channel, 'What are the options?')

@command
async def link(client, message):
    """Get links to Pimoroni resources."""
    links = {
        'shop': ('Pimoroni shop', 'https://shop.pimoroni.com/'),
        'learn': ('Pimoroni Yarr-niversity', 'https://learn.pimoroni.com/'),
        'blog':  ('Pimoroni blog', 'https://blog.pimoroni.com/'),
        'forum': ('Pimoroni forums', 'https://forums.pimoroni.com/'),
        'twitter': ('Pimoroni Twitter', 'https://twitter.com/pimoroni'),
        'youtube': ('Pimoroni YouTube channel', 'https://youtube.com/pimoroniltd'),
        'about': ('Pimoroni "about us" page', 'https://shop.pimoroni.com/pages/about-us')
    }
    messages = ['The {} is at: {}', "Here's a link to the {}: {}", 'The {} can be found at: {}']

    try:
        link = message.content.split()[1].lower()
    except IndexError:
        await client.send_message(message.channel, 'Which link do you want? {}'.format(', '.join(l for l in links)))
    else:
        try:
            await client.send_message(message.channel, random.choice(messages).format(*links[link]))
        except KeyError:
            await client.send_message(message.channel, "I don't know where that is. Try one of these: {}".format(', '.join(l for l in links)))


@command
@authorized
async def checkauth(client, message):
    """Test command to check whether you are authorized. (Requires authorization.)"""
    await client.send_message(message.channel, 'Congratulations, you are authorized.')
