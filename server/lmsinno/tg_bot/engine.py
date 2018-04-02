# TODO Telegram bot for Librarian
import requests as rq
from ..const import BOT_KEY


def send_message(user, msg):
    link = 'https://api.telegram.org/bot'+BOT_KEY+'/sendMessage?chat_id=' + str(user) + '&text=' + msg
    rq.get(link)


def get_update():
    url = 'https://api.telegram.org/bot'+BOT_KEY+'/getUpdates'
    response = rq.get(url)
    if response.json()['ok'] == 'true':
        return response.json()['result']
    return None
