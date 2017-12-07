import asyncio
import requests
import itertools
import emoji

from pimodisco.classify.classify import run_inference_on_image

reactions = set(e[1:-1].lower() for e in itertools.chain(emoji.EMOJI_UNICODE.keys(), emoji.EMOJI_ALIAS_UNICODE.keys()))

async def react_to_image(client, message):
    await asyncio.sleep(5)
    for e in message.embeds:
        print(e)
        if e['type'] == 'image':
            print(e['url'])
            result = run_inference_on_image(requests.get(e['thumbnail']['url']).content)
            for (p,s) in result:
                if s > 0.1:
                    words = p.split()
                    for word in words:
                        word = word.strip().replace(',', '').lower()
                        if word in reactions:
                            shortcode = ':{}:'.format(word)
                            emj = emoji.emojize(shortcode, use_aliases=True)
                            print(shortcode, emj)
                            await client.add_reaction(message, emj)
                            return