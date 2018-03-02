import os
import requests

try:
    from urllib import quote_plus
except ImportError:
    from urllib.parse import quote_plus

baseurl = 'https://www.googleapis.com/youtube/v3'

api_key = os.environ.get('YOUTUBE_SERVER_API_KEY')
if not api_key:
    try:
        api_key = open('youtube.txt').read().strip()
    except Exception:
        print('Please put Youtube API key in youtube.txt or set the environment variable YOUTUBE_SERVER_API_KEY.')
        raise ImportError


def setup(bot):

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
            url = baseurl + '/search?part=snippet&type=video&channelId={}&maxResults=1&q={}&key={}'.format(
                'UCuiDNTaTdPTGZZzHm0iriGQ', quote_plus(query), api_key
            )
            result = requests.get(url).json()['items']
        except Exception as e:
            print(e)
            await ctx.send("Sorry, there was a problem communicating with YouTube.")
            return

        try:
            best = result[0]
        except IndexError:
            await ctx.send("Sorry, I couldn't find anything matching that description.")
            return

        await ctx.send('{}: https://youtube.com/watch?v={}'.format(
            best['snippet']['title'], best['id']['videoId']
        ))
