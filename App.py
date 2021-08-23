import os
import requests
import json
from stravalib.client import Client

class App:

    @staticmethod
    def upload(filename):
        """ Uploads an activity to strava """

        url = "https://www.strava.com/api/v3/uploads"
        token = App.get_token()

        header = {"Authorization": "Bearer " + token}
        param = {"file": f"new_activities\\{filename}", "data_type": "fit"}

        requests.post(url, headers=header, params=param)

        """token = App.get_token()

        strava = Client()
        strava.access_token = token    
        
        strava.upload_activity(activity_file=f"new_activities\\{filename}", data_type="fit")"""


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
        """ Returns the filenames of new activities """
        new_activities = []
        for filename in os.listdir("new_activities"):
            if (filename.endswith(".fit")):
                new_activities.append(filename)
        return new_activities


    @staticmethod
    def move_file(filename):
        """ Moves the activity file to another directory """
        pass


filename = App.get_new_activities()[0]

App.upload(filename)

#App.get_user_config()



