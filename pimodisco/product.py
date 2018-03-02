import os

from algoliasearch import algoliasearch

from discord.ext import commands

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
        if query == None:
            await ctx.send("What do you want to search for?")
        else:
            try:
                result = index.search(query, {'hitsPerPage': 1, 'attributesToRetrieve': 'title,handle,stock_description,price'})['hits']
            except Exception:
                await ctx.send("Sorry, there was a problem communicating with the Pimoroni store.")
            else:
                try:
                    best = result[0]
                except IndexError:
                    await ctx.send("Sorry, I couldn't find anything matching that description.")
                else:
                    await ctx.send('{}, {} for £{} each, https://shop.pimoroni.com/products/{}'.format(
                        best['title'], best['stock_description'], best['price'], best['handle']
                    ))
