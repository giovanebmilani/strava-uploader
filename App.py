import os
import requests
import json
from stravalib.client import Client

class App:

    @staticmethod
    def upload(activity):
        """ Uploads an activity to strava """
        token = App.get_token()

        strava = Client()
        strava.access_token = token

        upload = strava.upload_activity(activity_file=activity, data_type="fit")


    @staticmethod
    def get_token():
        """ Gets the auth token """
        url = "https://www.strava.com/api/v3/oauth/token"
        
        payload = App.get_user_config()
        payload["grant_type"]= "refresh_token"
        payload["f"] = "json"
       
        print("\nRequesting token...")

        response = requests.post(url, data=payload, verify=False)
        return response.json()["access_token"]

    @staticmethod
    def get_user_config():
        try:
            with open("config.json") as file:
                config = json.load(file)
        except:
            error = Exception("Set up settings first, use 'config' for more information.")
            exit(error)

        else:
            try:
                config["client_id"]
                config["client_secret"]
                config["refresh_token"]

            except Exception as error:
                print("Insufficient info provided")
                exit(f"{error} needs to be configured")
            
            else:
                return config

    @staticmethod
    def get_new_activities():
        """ Gets a new activity in directory """
        new_activities = []
        for filename in os.listdir("new_activities"):
            if (filename.endswith(".fit")):
                activity = open(f"new_activities\{filename}", "r", encoding="utf-8")
                new_activities.append(activity)
        return new_activities


    @staticmethod
    def move_file(filename):
        """ Moves the activity file to another directory """
        pass


#activity = App.get_new_activities()[0]
#print(activity)

#App.upload(activity)

App.get_user_config()



