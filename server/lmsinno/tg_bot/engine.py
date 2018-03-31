# TODO Telegram bot for Librarian
import requests as rq


def send_message(user, msg):
    print(rq.get('https://oauth.telegram.org/auth/get?bot_id=563324296&origin=https%3A%2F%2Ftrainno.ru'))
    link = 'https://api.telegram.org/bot563324296:AAG6dtFZk9Sh3IG2_RIOJ5ltPrradgEOmEw/sendMessage?chat_id=' + user + '&text=' + msg
    rq.get(link)


def get_update():
    url = 'https://api.telegram.org/bot563324296:AAG6dtFZk9Sh3IG2_RIOJ5ltPrradgEOmEw/getUpdates'
    response = rq.get(url)
    if response.json()['ok']:
        return response.json()['result']
    return None
