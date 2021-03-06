import logging
logger = logging.getLogger(__name__)

try:
    from urllib import quote_plus
except ImportError:
    from urllib.parse import quote_plus


def setup_args(parser):
    parser.add_argument('-y', '--youtube', metavar='API_KEY', default=None,
                        env_var='YOUTUBE_SERVER_API_KEY', help='Youtube API key.')


def setup(bot, args):
    if args.youtube is None:
        logger.warning('No Youtube API key supplied. Youtube search is disabled.')
        return


    @bot.command()
    async def youtube(ctx, *, query: str = None):
        """
        Search the Pimoroni YouTube channel.
        If no query, prints a link to the main channel.
        """
        if query is None:
            await ctx.send("The Pimoroni YouTube is at: https://youtube.com/pimoronilitd")
            return

        try:
            url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&channelId={}&maxResults=1&q={}&key={}'
            async with bot.aiohttp.get(url.format('UCuiDNTaTdPTGZZzHm0iriGQ', quote_plus(query), args.youtube)) as repl:
                best = (await repl.json())['items'][0]
        except IndexError:
            await ctx.send("Sorry, I couldn't find anything matching that description.")
            return
        except Exception as e:
            await ctx.send("Sorry, there was a problem communicating with YouTube.")
            raise

        await ctx.send('{}: https://youtube.com/watch?v={}'.format(
            best['snippet']['title'], best['id']['videoId']
        ))
