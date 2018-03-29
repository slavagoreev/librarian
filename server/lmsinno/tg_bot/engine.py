# TODO Telegram bot for Librarian
import requests as rq

def send_message(chat_id, msg):
    link = 'https://api.telegram.org/bot563324296:AAG6dtFZk9Sh3IG2_RIOJ5ltPrradgEOmEw/sendMessage?chat_id=' + str(chat_id) + '&text=' + msg
    rq.get(link)