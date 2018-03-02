import requests
from requests.auth import HTTPBasicAuth

try:
    from urllib import quote_plus
except ImportError:
    from urllib.parse import quote_plus

from discord.ext import commands

try:
    auth = HTTPBasicAuth(*os.environ.get('GITHUB_CREDENTIALS').split(','))
except Exception:
    try:
        auth = HTTPBasicAuth(*open('github.txt').read().strip().split(','))
    except Exception:
        print('Please put GitHub credentials in github.txt or set the environment variable GITHUB_CREDENTIALS, as "user,api_key".')
        print('GitHub will be rate limited.')
        auth = None


def setup(bot):
    @bot.command()
    async def github(ctx, *, query: str = None):
        """Get a link to a Pimoroni GitHub repository for a particular product.

        Usage: github [<query>]
           - searches the Pimoroni GitHub for a repository matching <query>.
             If no query, prints a link to the main page.
        """
        if query == None:
            await ctx.send("The Pimoroni GitHub is at: https://github.com/pimoroni")
        else:
            try:
                url = 'https://api.github.com/search/repositories?q=user:pimoroni+{}'.format(quote_plus(query))
                result = requests.get(url, auth=auth).json()['items']
            except Exception as e:
                print(e)
                await ctx.send("Sorry, there was a problem communicating with GitHub.")
            else:
                try:
                    best = result[0]
                except IndexError:
                    await ctx.send("Sorry, I couldn't find anything matching that description.")
                else:
                    await ctx.send('{}: {}'.format(best['description'], best['html_url']))

    @bot.command(hidden=True)
    @commands.is_owner()
    async def ratelimit(ctx):
        rl = requests.get('https://api.github.com/rate_limit', auth=auth).json()
        await ctx.send(rl)