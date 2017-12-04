import os
import requests

from pimodisco.commands import command

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

@command
async def youtube(client, message):
    """Search the Pimoroni YouTube channel.

    Usage: youtube [<query>]
       - searches the Pimoroni YouTube for a video matching <query>.
         If no query, prints a link to the main channel.
    """
    try:
        query = message.content.split(maxsplit=1)[1]
    except IndexError:
        await client.send_message(message.channel, "The Pimoroni YouTube is at: https://youtube.com/pimoronilitd")
    else:
        try:
            url = baseurl + '/search?part=snippet&type=video&channelId={}&maxResults=1&q={}&key={}'.format(
                'UCuiDNTaTdPTGZZzHm0iriGQ', quote_plus(query), api_key
            )
            result = requests.get(url).json()['items']
        except Exception as e:
            print(e)
            await client.send_message(message.channel, "Sorry, there was a problem communicating with YouTube.")
        else:
            try:
                best = result[0]
            except IndexError:
                await client.send_message(message.channel, "Sorry, I couldn't find anything matching that description.")
            else:
                await client.send_message(message.channel, '{}: https://youtube.com/watch?v={}'.format(
                    best['snippet']['title'], best['id']['videoId']
                ) )

