from flask import Flask, request
import requests
import os
import time

server = Flask(__name__)

client_id = '69535'
client_secret = 'bac246d8c108ae3a6f7682be186105d513e33727'

upload_url = 'https://www.strava.com/api/v3/uploads'

@server.get('/authorized')
def get_auth_code():
    auth_code = request.args.get('code')
    return token_exchange(auth_code)
     

def token_exchange(auth_code):
    res = requests.post('https://www.strava.com/oauth/token?client_id='+client_id+'&client_secret='+client_secret+'&code='+auth_code+'&grant_type=authorization_code')
    token = res.json()['access_token']
    return upload(token)


def upload(token):
    new_activities = get_new_activities()
    if len(new_activities) > 0:
        print(f'Were found {len(new_activities)} new activities to upload.<br>Uploading ...')
        #responses = []
        for activity in new_activities:
            header = {'Authorization': 'Bearer ' + token}
            param = {'activity_type': 'ride', 'data_type': 'fit'}
            file = {'file': activity}
            res = requests.post(upload_url, headers=header, data=param, files=file)
            print(res.json())
        return 'Checking...'#check(responses, token)
    return 'No activities to upload.'

"""def check(responses, token):
    time.sleep(3)
    header = {'Authorization': 'Bearer ' + token}
    for res in responses:
        params = {'id': res.json()['id_str']}
        upload = requests.get(url=f'https://www.strava.com/api/v3/uploads', headers=header, data=params)
        print(upload.json())
    return 'Checking...'"""

def get_new_activities():
    new_activities = []
    for filename in os.listdir('activities'):
        if (filename.endswith('.fit')):
            #new_activities.append(filename)
            activity = open(f'activities/{filename}', 'rb')
            new_activities.append(activity)
    return new_activities

if __name__ == '__main__':
    server.run()
