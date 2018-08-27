import requests
from time import sleep


url = "https://api.telegram.org/bot631876179:AAGjUZtcbh60nw2zpEjCKKIRKlw5l5NpKog/"


def get_updates_json(request):  
    params = {'timeout':100, 'offset':None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()


def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def main(message):  
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
            send_mess(get_chat_id(last_update(get_updates_json(url))), message)
            update_id += 1
            sleep(1)       

message = 'Hello world!' 
main(message)



