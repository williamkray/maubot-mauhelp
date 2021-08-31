from maubot import Plugin, MessageEvent
from maubot.handlers import command
from mautrix.types import EventType


class MauHelp(Plugin):
    @command.new(name="help", help="Shows this help text")
    async def help(self, evt: MessageEvent):
        help_text = ''
        for handler_func, wait_sync in self.client.event_handlers[EventType.ROOM_MESSAGE]:
            if hasattr(handler_func, '__mb_name__') and hasattr(handler_func, '__mb_usage_inline__'):
                help_text += f"{handler_func.__mb_usage_inline__}\n"

        await evt.reply(help_text)
