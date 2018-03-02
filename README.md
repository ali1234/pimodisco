# Pimoroni-Discord-Bot
This is the officially unofficial Pimoroni Discord bot!

Feel free to mess around with the code and make improvements where you
can!


# Install

Run `pip3 install -r requirements.txt` from the root of the repository
to install pimodisco and all dependencies.


# Running
In order to run this bot for yourself, you need:
- A Discord server within which you have permission to add a bot.
- An bot application, which can be created here:
    https://discordapp.com/developers/applications/me
- A bot token.
- A bot client ID.

In order to add the bot to a server, simply navigate to
    https://discordapp.com/api/oauth2/authorize?client_id=[CLIENT ID]&scope=bot&permissions=0, replacing [CLIENT ID] with your bot's client ID.

Place the bot token into `discord.txt` in the current directory where
you run the bot, or put it in the environment variable
`DISCORD_BOT_TOKEN`.

To use all the features you also need some other API credentials:

- `ALGOLIA_CREDENTIALS=app_id,api_key`, or place in `algolia.txt`.
- `YOUTUBE_SERVER_API_KEY=key`, or place in `youtube.txt`.
- `GITHUB_CREDENTIALS=user,api_key` or place in `github.txt`.


# Extending
To create new commands, define an async function and add the `@command`
decorator. The name of the function will be the name of the command.

To make the command completely secret, also add the `@secret` decorator.
It will not appear on `!help` and `!help` command will return an error.
If the command is authorized and an unauthorized user attempts to run
it, an unknown command error message will be given, rather than a
permission error.

To add synonyms to a command, add the `@synonyms` decorator. This takes
a variable number of arguments. Each should be a string giving one
synonym for the command.

To limit a command to authorized users, add the @authorized decorator.
The `@authorized` decorator should always be placed after any
`@command`, `@secret` or `@synonym` decorators.

You can add commands to `pimodisco/commands.py`, or import the
decorators into your own module. If you do the latter you must import
your module in `__init__.py` in order to make the decorators register
your command.

The first line of the function's docstring will be used for short help
on the `!help` command. The whole docstring is displayed if a user
types `!help <function>`.

Commands must accept two arguments: the Discord client and message.

Example:

    from pimodisco.commands import command, synonyms, secret, authorized
    import datetime

    @command
    @synonyms('date', 'now')
    @secret
    @authorized
    async def time(client, message):
        '''Show the time.'''
        await client.send_message(
            message.channel,
            '{}, it is {}.'.format(
                message.author.mention,
                datetime.datetime.now(),
            )
        )