import requests
import base64
import json
import re
import unicodedata
import markdown
import yaml
import pathlib

from collections import defaultdict

try:
    from urllib import quote_plus
except ImportError:
    from urllib.parse import quote_plus

from discord.ext import commands
from pimodisco.github import auth


def slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    return re.sub('[-\s]+', '_', value)


def loads(markson):
    '''
    Loads and parses JSON-embedded Markdown file, chopping out and
    parsing any JSON contained therein.
    Returns an object that includes the JSON data, and the parsed HTML.
    '''

    markson = markson.replace('\r','')

    _data = re.search(re.compile(r'<!--(JSON:|\n---\n)(.*)-->', re.DOTALL), markson)

    _markdown = re.sub(re.compile(r'<!--(JSON:|\n---\n)(.*)-->', re.DOTALL), '', markson)
    _html = markdown.markdown(_markdown, extensions=['fenced_code'])

    # Scan for the Title in the Markdown file, this is always assumed
    # to be the first string starting with a single hash/pound ( # ) sign
    _title = re.search(re.compile(r'^#[^\#](.*)$', re.MULTILINE), markson)

    if _title != None:
        _title = _title.group(0).replace('#', '').strip()

    if _data != None:
        _type = _data.group(0)[4:8].upper().strip()

        if _type == 'JSON':
            _data = re.search('\{(.*)\}', _data.group(0), re.DOTALL).group(0)
            _data = json.loads(_data)
        elif _type == '---':
            _data = re.search('\n(.*)\n', _data.group(0), re.DOTALL).group(0)
            _data = yaml.load(_data)
        else:
            data = {}

        _data['title'] = _title

    elif _title != None:
        _data = {'title':_title}

    return {'data':_data, 'html':_html}

def get_board_raw(query):
    url = 'https://api.github.com/search/code?q=repo:gadgetoid/pinout.xyz+path:src/en/overlay+{}'.format(
        quote_plus(query))
    result = requests.get(url, auth=auth).json()['items']
    url = 'https://api.pinout.xyz/v1/md/{}'.format(pathlib.Path(result[0]['path']).name)
    yaml = requests.get(url).content
    return loads(yaml.decode('utf-8'))


def setup(bot):

    @bot.command()
    async def pinout(ctx, *, query: str = None):
        """Search Pinout.xyz for a particular product.

        Usage: pinout [<query>]
           - searches Pinout.xyz for a board matching <query>.
             If no query, prints a link to the main page.
        """
        if query is None:
            await ctx.send("Pinout.xyz is at: https://pinout.xyz")
        else:
            try:
                raw = get_board_raw(query)
            except KeyError:
                await ctx.send("Sorry, there was a problem communicating with GitHub.")
            except IndexError:
                await ctx.send("Sorry, I couldn't find anything matching that description.")
            else:
                await ctx.send('{} {}: https://pinout.xyz/pinout/{}#'.format(
                    raw['data']['manufacturer'], raw['data']['title'], slugify(raw['data']['name'])
                ))

    @bot.command(aliases=['hatstack'])
    async def phatstack(ctx):
        """Check compatibility between boards using Pinout.xyz

        Usage: pinout <query> [/ <query> / ...]
           - Supply a list of up to six boards separated with '/'.
             A list of pin/i2c address collisions will be displayed.
             Pinout.xyz is crowdsourced and results may be innaccurate.
        """
        async with ctx.typing():
            try:
                query = ctx.message.content.split(maxsplit=1)[1].split('/')
                if len(query) > 6:
                    await ctx.send("Can't compare more than six boards.")
                    return
            except IndexError:
                await ctx.send("Please specify boards separated by '/'.")
            else:
                try:
                    boards = []
                    for q in query:
                        q = q.strip()
                        if q == '':
                            continue
                        boards.append(get_board_raw(q.strip()))
                    if len(boards) == 0:
                        await ctx.send("Please specify boards separated by '/'.")
                        return
                except KeyError:
                    await ctx.send('Sorry, there was a problem communicating with GitHub.')
                except IndexError:
                    await ctx.send("Sorry, I couldn't find anything matching that description.")
                else:
                    overlap = defaultdict(list)
                    for b in boards:
                        for i in range(1, 41):
                            if str(i) in b['data']['pin']:
                                try:
                                    fnc = b['data']['pin'][str(i)]['mode']
                                except KeyError:
                                    try:
                                        fnc = b['data']['pin'][str(i)]['name']
                                    except KeyError:
                                        fnc = 'Unknown'
                                finally:
                                    if fnc != 'i2c':
                                        overlap[i].append('{} ({})'.format(b['data']['title'], fnc))

                    i2caddr = defaultdict(list)
                    for b in boards:
                        if 'i2c' in b['data']:
                            for addr in b['data']['i2c'].keys():
                                i2caddr[addr].append(b['data']['title'])

                    await ctx.send('Selected boards:\n\n{}\n\n{}\n\n{}\n{}'.format(
                        '\n'.join('{} {}'.format(
                            b['data']['manufacturer'],
                            b['data']['title']
                        ) for b in boards),
                        'Collisions:' if (any(len(o) > 1 for o in overlap.values()) or any(len(o) > 1 for o in i2caddr.values())) else 'Boards are compatible.',
                        '\n'.join('Pin {}: {}'.format(k, ', '.join(v)) for k, v in overlap.items() if len(v) > 1),
                        '\n'.join('I2C Address {}: {}'.format(k, ', '.join(v)) for k, v in i2caddr.items() if len(v) > 1)
                    ))


