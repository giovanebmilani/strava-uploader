from flask import render_template, request, Blueprint
from app import config
import requests
import os
import time
import shutil

api_upload = Blueprint('api_upload', __name__)

uploaded = []

@api_upload.route('/activities')
def activities():
    activities = _get_new_activities_filenames()
    return render_template('activities.html', activities=activities, uploaded=uploaded)

def _get_new_activities_filenames():
    new_activities = []
    for filename in os.listdir('activities'):
        if (filename.endswith('.fit')):
            new_activities.append(filename)
    return new_activities

@api_upload.route('/upload', methods=['POST'])
def upload():
    activity = _get_activity_file(request.form.get('filename'))
    header = {'Authorization': 'Bearer ' + os.getenv('USER_ACCESS_TOKEN') }
    param = {'name': request.form.get('name'), 'description': request.form.get('description'), 'activity_type': request.form.get('activity_type'), 'data_type': 'fit'}
    file = {'file': activity}
    res = requests.post(config.STRAVA_UPLOAD_URL, headers=header, data=param, files=file)
    status = _check_upload(res.json()['id_str'])
    uploaded.append({'file': request.form.get('filename'), 'status': status})
    activity.close()
    _move_file(request.form.get('filename'))
    return activities()

def _get_activity_file(filename):
    for file in os.listdir('activities'):
        if (file == filename):
            activity = open(f'activities/{filename}', 'rb')
    return activity

def _check_upload(upload_id):
    header = {'Authorization': 'Bearer ' + os.getenv('USER_ACCESS_TOKEN') }
    while True:
        upload = requests.get(config.STRAVA_UPLOAD_URL+'/'+upload_id, headers=header)
        if upload.json()['status'] == 'Your activity is ready.':
            return upload.json()['status']
        elif upload.json()['error'] is not None:
            return upload.json()['error']
        time.sleep(1.5)

def _move_file(filename):
    for file in os.listdir('activities'):
        if (file == filename):
            shutil.move(f'activities\\{filename}', 'activities\\uploaded')