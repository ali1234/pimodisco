from aiohttp import BasicAuth

import logging
logger = logging.getLogger(__name__)

try:
    from urllib import quote_plus
except ImportError:
    from urllib.parse import quote_plus

from discord.ext import commands

from pimodisco.checks import authCheck


auth = None


def setup_args(parser):
    parser.add_argument('-g', '--github', nargs=2, type=str, metavar=('USER','API_KEY'), default=None, env_var='GITHUB_CREDENTIALS', help='GitHub credentials.')


def setup(bot, args):
    global auth
    if args.github is None:
        logger.warning('No GitHub credentials supplied. GitHub searches will be rate limited.')
    else:
        auth = BasicAuth(*args.github)

    @bot.command()
    async def github(ctx, *, query: str = None):
        """
        Get a link to a Pimoroni GitHub repository for a particular product.
        If no query, prints a link to the main page.
        """
        if query is None:
            await ctx.send("The Pimoroni GitHub is at: https://github.com/pimoroni")
            return

        try:
            url = 'https://api.github.com/search/repositories?q=user:pimoroni+{}'.format(quote_plus(query))
            async with bot.aiohttp.get(url, auth=auth) as repl:
                best = (await repl.json())['items'][0]
        except IndexError:
            await ctx.send("Sorry, I couldn't find anything matching that description.")
            return
        except Exception as e:
            await ctx.send("Sorry, there was a problem communicating with GitHub.")
            raise

        await ctx.send('{}: {}'.format(best['description'], best['html_url']))

    @bot.command(hidden=True)
    @commands.check(authCheck)
    async def ratelimit(ctx):
        async with bot.aiohttp.get('https://api.github.com/rate_limit', auth=auth) as resp:
            rl = await resp.json()
        await ctx.send(rl)
