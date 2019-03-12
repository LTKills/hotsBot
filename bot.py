from bottle import run, post, request as bottle_request
import requests

bot_token = '702304671:AAFXVoC1Ev_SBnfHzQR_TOjoCCaveMka6Lg'
api_url = 'https://api.telegram.org/bot'

def getChatId(data):
    return data['message']['from']['id']

def getMessageText(data):
    return data['message']['text']

def sendMsg(msg, chat_id):
    send = api_url + bot_token + '/' + 'sendMessage?chat_id=' + \
        str(chat_id) + '&text=' + msg
    requests.get(send)
    pass


@post('/702304671:AAFXVoC1Ev_SBnfHzQR_TOjoCCaveMka6Lg/')
def main():
    data = bottle_request.json
    chat_id = getChatId(data)
    text = getMessageText(data)

    sendMsg(text[::-1], chat_id)

    return


if __name__ == '__main__':
    if os.environ.get('APP_LOCATION') == 'heroku':
        run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        run(host='localhost', port=8080, debug=True)
