import os
import shutil
import requests
import json
from stravalib.client import Client

class Uploader:

    @staticmethod
    def upload(filename):
        """ Uploads an activity to strava """
        token = Uploader.get_token()

        url = "https://www.strava.com/api/v3/uploads"
        header = {"Authorization": "Bearer " + token}
        param = {"file": f"new_activities\\{filename}", "data_type": "fit"}

        try:
            upload = requests.post(url, headers=header, params=param)
        except Exception as error:
            exit(error)

        

    @staticmethod
    def get_token():
        """ Gets the auth token """
        url = "https://www.strava.com/api/v3/oauth/token"
        
        payload = Uploader.get_user_config()
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
            raise ("Set up settings first, use 'config' for more information.")

        else:
            try:
                config["client_id"]
                config["client_secret"]
                config["refresh_token"]

            except Exception as error:
                raise (f"Insufficient info provided. {error} needs to be configured")
            
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
        shutil.move(f"new_activities\\{filename}", "uploaded_activities")


def main():
    filename = Uploader.get_new_activities()[0]
    print(filename)
    #Uploader.upload(filename)
    #Uploader.move_file(filename)

    """new_activities_filenames = Uploader.get_new_activities()

    for filename in new_activities_filenames:
        try:
            Uploader.upload(filename)
        except Exception as error:
            exit(error)"""
    

if __name__ == "__main__":
    main()





