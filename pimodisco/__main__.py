import discord
import asyncio


from pimodisco.commands import commands, cmd_prefix
from pimodisco.filter import filter

# modules which contain commands must be imported, even though we don't use them directly.
# importing them causes them to register with pimodisco.commands.

try:
    import pimodisco.product
except ImportError:
    print('Product search not available.')

try:
    token = open('token.txt').read().strip()
except Exception:
    print('Please put Discord bot token in token.txt.')
    exit(-1)

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if await filter(client, message):
        # something bad about this message, so ignore it.
        pass
    elif message.content.startswith(cmd_prefix):
        parsed = message.content.split(maxsplit=1)
        try:
            await commands[parsed[0][1:].lower()](client, message)
        except KeyError:
            await client.send_message(message.channel, "I don't know that command. Type !help for a list of commands.")

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


if __name__ == '__main__':
    main()



