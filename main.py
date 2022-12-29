from telethon import TelegramClient
from telethon.tl.functions.account import UpdateUsernameRequest
import threading, requests, time, random

# you should use your own api_hash and api_id
api_hash = 'your_api_hash' 
api_id = 123

state = False
time1 = time.time()
new_username = ''
result = None

def check_username():
    global new_username, state, time1, result

    while True:
        r = requests.get('https://t.me/' + new_username)

        if 'shine' in r.text:
            result = 0

        if result != 0:
            time1 = time.time()
            state = True
            break
        elif r.status_code == 200 and result == 0:
            print("checking username {0}".format('.'*random.randrange(1, 5)+' '*5), end="\r")
        else:
            print('no response from telegram')


new_username = input('enter target username: ')

client = TelegramClient('session_file', api_id, api_hash).start()

t = threading.Thread(target=check_username)
t.setDaemon(True)
t.start()

while True:
    if state == True:
        client(UpdateUsernameRequest(new_username))
        print('username changed in {0:.2f} seconds after last check.'.format(time.time() - time1))
        break

input('press enter to exit')
