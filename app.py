from flask import Flask, render_template, request, redirect
from config import config_by_name
from datetime import datetime, timedelta
import requests
import os
import shutil

app = Flask(__name__)
config = config_by_name['local']


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/auth')
def auth():
    return redirect(_get_auth_url())

def _get_auth_url():
    scopes = 'activity:write,read_all,activity:read_all'
    return config.STRAVA_AUTH_URL+'?'+'client_id='+config.CLIENT_ID+'&response_type=code&redirect_uri='+config.REDIRECT_URI+'&approval_prompt=force&scope='+scopes

@app.get('/authorized')
def get_auth_code():
    res = _token_exchange(request.args.get('code')) 
    return render_template('authenticating.html', result=res)

def _token_exchange(auth_code):
    try:
        res = requests.post(config.STRAVA_TOKEN_REQUEST_URL+'?client_id='+config.CLIENT_ID+'&client_secret='+config.CLIENT_SECRET+'&code='+auth_code+'&grant_type=authorization_code')
        os.environ['USER_ACCESS_TOKEN'] = str(res.json()['access_token'])
        os.environ['USER_REFRESH_TOKEN'] = str(res.json()['refresh_token'])
        os.environ['TOKEN_EXPIRES_AT'] = str(res.json()['expires_at'])
        return True
    except:
        return False
    
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
