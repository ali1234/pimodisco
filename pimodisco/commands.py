import random
import ast

from pimodisco import version as version__
from pimodisco import source_url
from pimodisco.checks import authCheck

from discord import TextChannel
from discord.ext import commands


def setup(bot):

    @bot.command(aliases=['hi'])
    async def hello(ctx):
        """
        Says hello back to you!
        """
        greetings = ['Hello', 'Hi', 'Greetings', "What's up"]
        await ctx.send('{} {}!'.format(random.choice(greetings), ctx.author.mention))

    @bot.command(aliases=['bye'])
    async def goodbye(ctx):
        """
        Says goodbye back to you!
        """
        goodbyes = ['Goodbye', 'See you', 'Later', 'Tata']
        await ctx.send('{} {}!'.format(random.choice(goodbyes), ctx.author.mention))

    @bot.command()
    async def version(ctx):
        """
        Says the currently active version of the bot.
        """
        await ctx.send('Version {}'.format(version__))

    @bot.command(aliases=['source'])
    async def code(ctx):
        """
        Prints a link to the bot's code.
        """
        await ctx.send("Here's a link to my source code: {}".format(source_url))

    @bot.command()
    async def roll(ctx, sides: int = 6):
        """
        Roll a n-sided die. (Default 6)
        """
        roll = random.randint(1, sides)
        await ctx.send('{} rolled!'.format(roll))

    @bot.command()
    async def choose(ctx, *choices):
        """
        Choose something from a list of options.
        """
        recommendations = ['Try', 'Go with', 'Maybe', 'Definitely', 'Consider', 'I asked @Gadgetoid and he said']
        if not choices:
            await ctx.send('Please give me some options to choose from.')
            return

        await ctx.send('{} {}.'.format(random.choice(recommendations), random.choice(choices)))

    @bot.command(aliases=['sum'])
    async def add(ctx, *numbers):
        """
        Add a list of numbers.
        """
        messages = ['Hmmm. {}.', 'Easy. {}.', 'That would be {}.', 'That equals {}.', "That's {}. Quick maths."]
        if not numbers:
            await ctx.send("Please give me some numbers to add up.")
            return

        # ast.literal_eval is safe for unknown inputs
        try:
            answer = sum(ast.literal_eval(n) for n in numbers)
        except Exception:
            await ctx.send("Something in there isn't a number, sorry.")
            return

        await ctx.send(random.choice(messages).format(answer))

    @bot.command()
    async def link(ctx, thing: str = None):
        """
        Get links to Pimoroni resources.
        """
        links = {
            'shop': ('Pimoroni shop', 'https://shop.pimoroni.com/'),
            'learn': ('Pimoroni Yarr-niversity', 'https://learn.pimoroni.com/'),
            'blog':  ('Pimoroni blog', 'https://blog.pimoroni.com/'),
            'forum': ('Pimoroni forums', 'https://forums.pimoroni.com/'),
            'twitter': ('Pimoroni Twitter', 'https://twitter.com/pimoroni'),
            'youtube': ('Pimoroni YouTube channel', 'https://youtube.com/pimoroniltd'),
            'about': ('Pimoroni "about us" page', 'https://shop.pimoroni.com/pages/about-us')
        }
        messages = ['The {} is at: {}', "Here's a link to the {}: {}", 'The {} can be found at: {}']

        if thing is None:
            await ctx.send("I can give you links for the following, please specify one.\n{}".format(', '.join(l for l in links)))
            return

        try:
            await ctx.send(random.choice(messages).format(*links[thing]))
        except KeyError:
            await ctx.send("I don't know where that is. Try one of these: {}".format(', '.join(l for l in links)))

    @bot.command(hidden=True)
    async def sudo(ctx):
        """
        A secret command. You will never see this help message.
        """
        words = ctx.message.content.split(maxsplit=4)
        params = ['make', 'me', 'a', 'sandwich']
        foods = [':croissant:', ':hamburger:', ':stuffed_pita:', ':hotdog:', ':bread:']
        ctx.messages = ['How about a {} instead?', 'Best I can do is {}']

        if len(words) == 5 and all(words[n+1] == params[n] for n in range(3)):
            if str(ctx.author) == 'Ryanteck#1989':
                await ctx.send("Okay {}, you're a sandwich.".format(ctx.author.mention))
            else:
                await ctx.send(random.choice(ctx.messages).format(random.choice(foods)))

    @bot.command()
    @commands.check(authCheck)
    async def checkauth(ctx):
        """
        Test command to check whether you are authorized.

        (Requires authorization).
        """
        await ctx.send('Congratulations, you are authorized.')

    @bot.command()
    @commands.check(authCheck)
    async def say(ctx, channel: TextChannel, *, message: str):
        """
        Send a message to a channel.

        (Requires authorization).
        """
        try:
            await channel.send(message)
        except:
            await ctx.send("Sadly I couldn't send a message to {}".format(channel.mention))
