import discord
import os


from pimodisco.commands import get_cmd, cmd_prefix
from pimodisco.filter import filter

# modules which contain commands must be imported, even though we don't use them directly.
# importing them causes them to register with pimodisco.commands.

import pimodisco.github
import pimodisco.pinout

from pimodisco.classify import react_to_image

try:
    import pimodisco.youtube
except ImportError:
    print('YouTube search not available.')

try:
    import pimodisco.product
except ImportError:
    print('Product search not available.')

token = os.environ.get('DISCORD_BOT_TOKEN')
if not token:
    try:
        token = open('discord.txt').read().strip()
    except Exception:
        print('Please put Discord bot token in discord.txt or set the environment variable DISCORD_BOT_TOKEN.')
        exit(-1)

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if await filter(client, message):
        # something bad about this message, so ignore it.
        pass
    else:
        if message.content.startswith(cmd_prefix):
            parsed = message.content.split(maxsplit=1)
            try:
                f = get_cmd(parsed[0][1:])
            except KeyError:
                await client.send_message(message.channel, "I don't know that command. Type !help for a list of commands.")
            else:
                await f(client, message)

        await react_to_image(client, message)


@client.event
async def on_member_join(member):
    pass
    #welcome = await client.send_message(discord.Object(general), "Welcome {} to the Officially Unofficial Pimoroni Discord Server!".format(member.mention))
    #await asyncio.sleep(5)
    #await client.delete_message(welcome)


@client.event
async def on_ready():
    print('Logged in as {} {}'.format(client.user.name, client.user.id))


def main():
    client.run(token)
    for x in client.get_all_emojis():
        print(x.name)


if __name__ == '__main__':
    main()



