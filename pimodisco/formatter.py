from __future__ import generator_stop

import asyncio

from discord.ext.commands.formatter import HelpFormatter


class Formatter(HelpFormatter):
    def get_ending_note(self):
        command_name = self.context.invoked_with
        return "Type {0}{1} <command> for more info on a command.\n".format(self.clean_prefix, command_name)

    @asyncio.coroutine
    def format_help_for(self, context, command_or_bot):
        ret = (yield from super().format_help_for(context, command_or_bot))
        return [s.replace('\u200bNo Category:', '\u200bCommands:') for s in ret]
