import discord
from discord.ext import commands
import random

description = '''A gool ol' Pimoroni Robot (Pirated)
                Please note, that since this bot runs in Python, all commands including a "space" must be inclosed in quotation marks!
                '''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# Basic Functions

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)
        
# Fun Stuff!

@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='PimoroniBot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, I am cool.')
    
@cool.command(name='Gadgetoid')
async def _bot():
    """Is Gadgetoid cool?"""
    await bot.say('Yes, Gadgetoid is cool.')
    
@cool.command(name='RaspberryPicardBox')
async def _bot():
    """Is RaspberryPicardBox cool?"""
    await bot.say('Yes, RaspberryPicardBox is cool.')
    
@bot.command()
async def EXPLODE():
    '''Don't type the red button!'''
    await bot.say("Ok...")
    await bot.say("EXPLOSION!")
    
# ------------The Real Beef------------

# None-priveleged Utilities

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

# Priveleged Utilities



# Final Run (Don't put code after this!)

bot.run('MzQ4MTczMjI1MTg5OTY1ODM1.DHjHrQ.bzmQ3l5UV87a5S-Y9dHtVRbURXs')