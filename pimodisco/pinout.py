import requests
import base64
import json
import re
import unicodedata
import markdown
import yaml

try:
    from urllib import quote_plus
except ImportError:
    from urllib.parse import quote_plus

from pimodisco.commands import command


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

@command
async def pinout(client, message):
    """Search Pinout.xyz for a particular product.

    Usage: pinout [<query>]
       - searches Pinout.xyz for a board matching <query>.
         If no query, prints a link to the main page.
    """
    try:
        query = message.content.split(maxsplit=1)[1]
    except IndexError:
        await client.send_message(message.channel, "Pinout.xyz is at: https://pinout.xyz")
    else:
        try:
            url = 'https://api.github.com/search/code?q=repo:gadgetoid/pinout.xyz+path:src/en/overlay+{}'.format(quote_plus(query))
            result = requests.get(url).json()['items']
            content = requests.get(result[0]['url']).json()['content']
            raw = loads((base64.b64decode(content).decode('utf-8')))
        except Exception as e:
            await client.send_message(message.channel, "Sorry, there was a problem communicating with GitHub.")
        else:
            try:
                best = result[0]
            except IndexError:
                await client.send_message(message.channel, "Sorry, I couldn't find anything matching that description.")
            else:

                await client.send_message(message.channel, '{} {}: https://pinout.xyz/pinout/{}#'.format(
                    raw['data']['manufacturer'], raw['data']['title'], slugify(raw['data']['name'])
                ) )
