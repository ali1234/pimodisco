from algoliasearch import algoliasearch

import logging
logger = logging.getLogger(__name__)


def setup_args(parser):
    parser.add_argument('-a', '--algolia', type=str, nargs=2, metavar=('APP_ID', 'API_KEY'), default=None, env_var='ALGOLIA_CREDENTIALS', help='Algolia credentials.')


def setup(bot, args):
    if args.algolia is None:
        logger.warning('No Algolia credentials supplied. Product search is disabled.')
        return
    else:
        search = algoliasearch.Client(*args.algolia)
        # algolia refuses service if referer is wrong. lol.
        search._transport.session.headers.update({'Referer': 'https://shop.pimoroni.com/'})
        index = search.init_index('shop.pimoroni.com.products')

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
            async with bot.aiohttp.get(url) as repl:
                json = await repl.json()
            stock = json['product']['variants'][0]['inventory_quantity']
            vendor = json['product']['vendor']
            if stock > 0:
                stock_msg = '{} in stock'.format(stock)
            else:
                stock_msg = 'out of stock'
        except IndexError:
            await ctx.send("Sorry, I couldn't find anything matching that description.")
            return
        except Exception as e:
            await ctx.send("Sorry, there was a problem communicating with the Pimoroni store.")
            raise

        await ctx.send('{} by {}, {}, £{} each, https://shop.pimoroni.com/products/{}'.format(
            best['title'], vendor, stock_msg, best['price'], best['handle']
        ))
