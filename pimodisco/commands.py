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
        print(roles)
        if any(role in roles for role in authorized_roles):
            await f(message)
        else:
            await client.send_message(message.channel, "You do not have permission to use this command.")
    checkauth.__name__ = f.__name__
    return checkauth


@command
async def help(client, message):
    """[<command>] : Prints help about commands. With no argument, prints general help."""
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
            ', '.join(f.__name__ for f in commands.values())
        ))

@command
async def about(client, message):
    await client.send_message(message.channel,"""```


```""".format(version))


@command
@authorized
async def checkauth(client, message):
    """Test command to check whether you are authorized. (Requires authorization.)"""
    await client.send_message(message.channel, 'Congratulations, you are authorized.')
