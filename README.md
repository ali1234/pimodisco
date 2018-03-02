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
