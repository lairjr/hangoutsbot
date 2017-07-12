import plugins

import os
import valve.source.a2s

def _initialise(bot):
    plugins.register_user_command(["cs_connect", "cs_info"])

def cs_connect(bot, event, *args):
    """
    Display CS connection string

    /bot cs_connect
    """

    yield from bot.coro_send_message(event.conv, "connect " + str(os.environ['HOST_IP']).strip())

def cs_info(bot, event, *args):
    """
    Display CS information

    /bot cs_connect
    """

    SERVER_ADDRESS = (str(os.environ['HOST_IP']).strip(), 27015)

    server = valve.source.a2s.ServerQuerier(SERVER_ADDRESS)
    info = server.info()
    players = server.players()

    html_text = '<b>Map: </b>{map}<br />'.format(**info)
    player_count = '{player_count}/{max_players}'.format(**info)
    html_text += '<b>Players: </b>' +  player_count + '<br /><br />'

    for player in sorted(players["players"], key=lambda p: p["score"], reverse=True):
        html_text += '{score} {name}<br />'.format(**player)

    yield from bot.coro_send_message(event.conv, html_text)
