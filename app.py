from flask import Flask, request
from config import config_by_name
import requests
import os
import shutil

app = Flask(__name__)
config = config_by_name['local']


@app.get('/authorized')
def get_auth_code():
    auth_code = request.args.get('code')
    return token_exchange(auth_code)
     

def token_exchange(auth_code):
    res = requests.post(config.STRAVA_TOKEN_REQUEST_URL+'?client_id='+config.CLIENT_ID+'&client_secret='+config.CLIENT_SECRET+'&code='+auth_code+'&grant_type=authorization_code')
    token = res.json()['access_token']
    return upload(token)


def upload(token):
    new_activities = get_new_activities()
    if len(new_activities) > 0:
        for activity in new_activities:
            header = {'Authorization': 'Bearer ' + token}
            param = {'activity_type': 'ride', 'data_type': 'fit'}
            file = {'file': activity}
            res = requests.post(config.STRAVA_UPLOAD_URL, headers=header, data=param, files=file)
            print(res.json())
        #move_files()
        return (f'Were found {len(new_activities)} new activities to upload.<br>Uploading ...')
    return 'No activities to upload.'


def get_new_activities():
    new_activities = []
    for filename in os.listdir('activities'):
        if (filename.endswith('.fit')):
            activity = open(f'activities/{filename}', 'rb')
            new_activities.append(activity)
    return new_activities


def move_files():
    for filename in os.listdir('activities'):
        if (filename.endswith('.fit')):
            shutil.move(f'activities\\{filename}', 'activities\\uploaded')


if __name__ == '__main__':
    app.run()
