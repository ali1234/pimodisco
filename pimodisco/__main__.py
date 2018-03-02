from discord.ext.commands import AutoShardedBot
import os

from pimodisco.filter import filter

token = os.environ.get('DISCORD_BOT_TOKEN')
if not token:
    try:
        token = open('discord.txt').read().strip()
    except Exception:
        print('Please put Discord bot token in discord.txt or set the environment variable DISCORD_BOT_TOKEN.')
        exit(-1)

extensions = [
    'pimodisco.commands',
    'pimodisco.github',
    'pimodisco.pinout',
    'pimodisco.product',
    'pimodisco.youtube',
]


def main():
    bot = AutoShardedBot(command_prefix='!')
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except ImportError:
            print('Extension {} failed to load. It has been disabled.'.format(extension))
            pass
    bot.run(token)

if __name__ == '__main__':
    main()



