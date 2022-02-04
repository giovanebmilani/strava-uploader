from flask import Flask, request
import requests
import os

server = Flask(__name__)

client_id = '69535'
client_secret = 'bac246d8c108ae3a6f7682be186105d513e33727'
#redirect_url = 'http://127.0.0.1:5000/authorized'


@server.get('/authorized')
def get_auth_code():
    auth_code = request.args.get('code')
    return token_exchange(auth_code)
     

def token_exchange(auth_code):
    res = requests.post('https://www.strava.com/oauth/token?client_id='+client_id+'&client_secret='+client_secret+'&code='+auth_code+'&grant_type=authorization_code')
    return upload(res.json()["access_token"])


def upload(token):
    return token


def get_new_activities():
    new_activities = []
    for filename in os.listdir('activities'):
        if (filename.endswith('.fit')):
            new_activities.append(filename)
    return new_activities


if __name__ == '__main__':
    new_activities = get_new_activities()
    
    server.run()
