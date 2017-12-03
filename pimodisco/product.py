import os

from algoliasearch import algoliasearch

from pimodisco.commands import command

try:
    cred = os.environ.get('ALGOLIA_CREDENTIALS').split(',')
except Exception:
    try:
        cred = open('algolia.txt').read().strip().split(',')
    except Exception:
        print('Please put algolia credentials in algolia.txt or set the environment variable ALGOLIA_CREDENTIALS, as "app_id,api_key".')
        raise ImportError


search = algoliasearch.Client(*cred)
# algolia refuses service if referer is wrong. lol.
search._transport.session.headers.update({'Referer': 'https://shop.pimoroni.com/'})
index = search.init_index('shop.pimoroni.com.products')

@command
async def product(client, message):
    """Search the Pimoroni store.

    Usage: product <query>
        <query> : string to search for. Spaces allowed. Returns stock level, price and link to the first hit.
    """
    try:
        query = message.content.split(maxsplit=1)[1]
    except IndexError:
        await client.send_message(message.channel, "What do you want to search for?")
    else:
        try:
            result = index.search(query, {'hitsPerPage': 1, 'attributesToRetrieve': 'title,handle,stock_description,price'})['hits']
        except Exception:
            await client.send_message(message.channel, "Sorry, there was a problem communicating with the Pimoroni store.")
        else:
            try:
                best = result[0]
            except IndexError:
                await client.send_message(message.channel, "Sorry, I couldn't find anything matching that description.")
            else:
                await client.send_message(message.channel, '{}, {} for £{} each, https://shop.pimoroni.com/products/{}'.format(
                    best['title'], best['stock_description'], best['price'], best['handle']
                ) )
