import plugins

import os

def _initialise(bot):
    plugins.register_user_command(["cs_connect"])

def cs_connect(bot, event, *args):
    """
    Display CS server ip

    /bot cs_connect
    """

    yield from bot.coro_send_message(event.conv, "connect " + str(os.environ['HOST_IP']).strip())
