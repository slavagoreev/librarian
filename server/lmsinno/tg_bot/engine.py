from ..const import BOT_KEY, HTTP_SESSION


def send_message(user, msg):
    link = 'https://api.telegram.org/bot'+BOT_KEY+'/sendMessage?chat_id=' + str(user) + '&text=' + msg
    HTTP_SESSION.get(link)


def get_update():
    url = 'https://api.telegram.org/bot'+BOT_KEY+'/getUpdates'
    response = HTTP_SESSION.get(url)
    if response.json()['ok']:
        return response.json()['result']
    return None
