import requests

try:
    from urllib import quote_plus
except ImportError:
    from urllib.parse import quote_plus

from pimodisco.commands import command

@command
async def github(client, message):
    """Get a link to a Pimoroni GitHub repository for a particular product.

    Usage: github [<query>]
       - searches the Pimoroni GitHub for a repository matching <query>.
         If no query, prints a link to the main page.
    """
    try:
        query = message.content.split(maxsplit=1)[1]
    except IndexError:
        await client.send_message(message.channel, "The Pimoroni GitHub is at: https://github.com/pimoroni")
    else:
        try:
            url = 'https://api.github.com/search/repositories?q=user:pimoroni+{}'.format(quote_plus(query))
            result = requests.get(url).json()['items']
        except Exception as e:
            print(e)
            await client.send_message(message.channel, "Sorry, there was a problem communicating with GitHub.")
        else:
            try:
                best = result[0]
            except IndexError:
                await client.send_message(message.channel, "Sorry, I couldn't find anything matching that description.")
            else:
                await client.send_message(message.channel, '{}: {}'.format(
                    best['description'], best['html_url']
                ) )
