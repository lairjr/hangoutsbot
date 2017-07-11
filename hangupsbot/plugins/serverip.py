import plugins

def _initialise(bot):
    plugins.register_user_command(["serverip"])

def serverip(bot, event, *args):
    """
    Display CS server ip

    /bot serverip
    """

    yield from bot.coro_send_message(event.conv, "Server connection: connect 10.0.01")
