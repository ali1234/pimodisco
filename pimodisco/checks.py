from discord.ext.commands import Context


async def authCheck(ctx: Context):
    """
    Checks if the user is auth'ed, by role id.
    """
    if hasattr(ctx.author, 'roles'):
        required_ids = []
        matches = [f for f in ctx.author.roles if f.id in required_ids]
        if matches:
            return True

    await ctx.send("Sorry, you do not have permission to use this command :(")
    return False
