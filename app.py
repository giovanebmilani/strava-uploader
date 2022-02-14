from flask import Flask, render_template, request, redirect
from config import config_by_name
import time
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
    auth_status = _get_auth_status()
    if auth_status == 'access token expired':
        res = _refresh_token()
        return render_template('authenticating.html', result=res)
    elif auth_status == 'no authentication':
        return redirect(_get_auth_url())
    else:
        return render_template('authenticating.html', result=True)

def _get_auth_status():
    if os.getenv('TOKEN_EXPIRES_AT') is not None:
        if time.time() > int(os.environ['TOKEN_EXPIRES_AT']):
            return 'access token expired'
        return 'authenticated'
    return 'no authentication'

def _refresh_token():
    try:
        res = requests.post(config.STRAVA_TOKEN_REQUEST_URL+'?client_id='+config.CLIENT_ID+'&client_secret='+os.getenv('USER_REFRESH_TOKEN')+'&grant_type=refresh_token'+config.CLIENT_SECRET+'&refresh_token')
        os.environ['USER_ACCESS_TOKEN'] = str(res.json()['access_token'])
        os.environ['USER_REFRESH_TOKEN'] = str(res.json()['refresh_token'])
        os.environ['TOKEN_EXPIRES_AT'] = str(res.json()['expires_at'])
        return True
    except:
        return False

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
    
@app.route('/activities')
def activities():
    activities = _get_new_activities_filenames()
    return render_template('activities.html', activities=activities)

def _get_new_activities_filenames():
    new_activities = []
    for filename in os.listdir('activities'):
        if (filename.endswith('.fit')):
            new_activities.append(filename)
    return new_activities

@app.post('/upload')
def upload(filename):
    activity = _get_activity_file(filename)
    header = {'Authorization': 'Bearer ' + os.getenv('USER_ACCESS_TOKEN') }
    param = {'activity_type': 'ride', 'data_type': 'fit'}
    file = {'file': activity}
    res = requests.post(config.STRAVA_UPLOAD_URL, headers=header, data=param, files=file)
    print(res.json())

def _get_activity_file(filename):
    for file in os.listdir('activities'):
        if (file == filename):
            activity = open(f'activities/{filename}', 'rb')
    return activity

def _move_file(filename):
    for file in os.listdir('activities'):
        if (file == filename):
            shutil.move(f'activities\\{filename}', 'activities\\uploaded')

if __name__ == '__main__':
    app.run()
