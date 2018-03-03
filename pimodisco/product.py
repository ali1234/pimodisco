import os
import requests

from algoliasearch import algoliasearch

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


def setup(bot):

    @bot.command(aliases=['shop'])
    async def product(ctx, *, query: str = None):
        """
        Search the Pimoroni store.
        Spaces allowed. Returns stock level, price and link to the first hit.
        """
        if query is None:
            await ctx.send("Please specify what you would like to search for.")
            return

        try:
            result = index.search(query, {'hitsPerPage': 1, 'attributesToRetrieve': 'title,handle,stock_description,price'})['hits']
            best = result[0]
            url = 'https://shop.pimoroni.com/products/{}.json'.format(best['handle'])
            json = requests.get(url).json()
            stock = json['product']['variants'][0]['inventory_quantity']
            vendor = json['product']['vendor']
            if stock > 0:
                stock_msg = '{} in stock'.format(stock)
            else:
                stock_msg = 'out of stock'
        except Exception:
            await ctx.send("Sorry, there was a problem communicating with the Pimoroni store.")
            return
        except IndexError:
            await ctx.send("Sorry, I couldn't find anything matching that description.")
            return

        await ctx.send('{} by {}, {}, £{} each, https://shop.pimoroni.com/products/{}'.format(
            best['title'], vendor, stock_msg, best['price'], best['handle']
        ))
