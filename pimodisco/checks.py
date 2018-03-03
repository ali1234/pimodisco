from discord.ext.commands import Context

import logging
logger = logging.getLogger(__name__)

auth_roles = []

async def authCheck(ctx: Context):
    """
    Checks if the user is auth'ed, by role id.
    """
    global auth_roles
    if hasattr(ctx.author, 'roles'):
        if any(f.id in auth_roles for f in ctx.author.roles):
            return True

    await ctx.send("Sorry, you do not have permission to use this command :(")
    return False


def setup_args(parser):
    parser.add_argument('-A', '--auth-roles', nargs='*', metavar='ID', env_var='AUTH_ROLES', help='Authorised role IDs.', type=int, default=[])


def setup(bot, args):
    global auth_roles
    auth_roles = args.auth_roles
    if len(auth_roles) == 0:
        logger.warning('No authorised roles defined. Authorised commands will not be available to anybody.')
    else:
        logger.info('Authorised roles: {}'.format(', '.join(str(r) for r in auth_roles)))
