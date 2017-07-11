import plugins

import os

def _initialise(bot):
    plugins.register_user_command(["serverip"])

def serverip(bot, event, *args):
    """
    Display CS server ip

    /bot serverip
    """

    yield from bot.coro_send_message(event.conv, "connect " + str(os.environ['HOST_IP']).strip())
