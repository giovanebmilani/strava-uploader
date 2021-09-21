import requests
import json



def upload(filename):
    pass


def authenticate():
    
    url = "https://www.strava.com/oauth/authorize"

    data = {}
    data["client_secret"] = 69535
    data["redirect_uri"] = "developers.strava.com"
    data["response_type"] = "code"
    data["scope"] = "activity:write"

    response = requests.get(url, data=data)
    return response


def token_exchange():
    pass



print(authenticate().json())