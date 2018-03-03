import logging
logger = logging.getLogger(__name__)

from importlib import import_module
from configargparse import ArgumentParser
from discord.ext.commands import AutoShardedBot


extensions = [
    'pimodisco.checks',
    'pimodisco.commands',
    'pimodisco.github',
    'pimodisco.pinout',
    'pimodisco.product',
    'pimodisco.youtube',
]


def main():
    parser = ArgumentParser()
    parser.add_argument('-c', '--config', required=True, is_config_file=True, help='Config file path.')
    parser.add_argument('-t', '--token', metavar='DISCORD_BOT_TOKEN', required=True, env_var='DISCORD_BOT_TOKEN', help='Discord bot token.')
    parser.add_argument('-p', '--prefix', metavar='COMMAND_PREFIX', default='!', env_var='COMMAND_PREFIX', help='Command prefix.')

    loaded_extensions = [import_module(e) for e in extensions]
    for e in loaded_extensions:
        e.setup_args(parser)

    args = parser.parse_args()

    bot = AutoShardedBot(command_prefix=args.prefix)
    for e in loaded_extensions:
        e.setup(bot, args)
    bot.run(args.token)

if __name__ == '__main__':
    main()



