from flask import Flask, request
import requests
import os
import json
from stravalib import Client

server = Flask(__name__)

client_id = '69535'
client_secret = 'bac246d8c108ae3a6f7682be186105d513e33727'
#redirect_url = 'http://127.0.0.1:5000/authorized'

upload_url = 'https://www.strava.com/api/v3/uploads'

@server.get('/authorized')
def get_auth_code():
    auth_code = request.args.get('code')
    return token_exchange(auth_code)
     

def token_exchange(auth_code):
    res = requests.post('https://www.strava.com/oauth/token?client_id='+client_id+'&client_secret='+client_secret+'&code='+auth_code+'&grant_type=authorization_code')
    return upload(res.json()['access_token'])


def upload(token):
    new_activities = get_new_activities()
    if len(new_activities) > 0:
        for filename in new_activities:
            with open(f"activities\{filename}", "rb") as activity:
                header = {'Authorization': 'Bearer ' + token}
                param = {'activity_type': 'ride', 'data_type': 'fit', 'file': activity}
                res = requests.post(upload_url, headers=header, params=param)
        return f'Were found {len(new_activities)} new activities to upload.<br>Uploading ...'

    return 'No activities to upload.'


def get_new_activities():
    new_activities = []
    for filename in os.listdir('activities'):
        if (filename.endswith('.fit')):
            new_activities.append(filename)
            """with open(f"activities\{filename}", "r", encoding="utf-8") as activity:
                new_activities.append(activity)"""
    return new_activities


if __name__ == '__main__':
    server.run()
