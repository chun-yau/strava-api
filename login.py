import requests
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("STRAVA_CLIENT_ID")
client_secret = os.getenv("STRAVA_CLIENT_SECRET")
refresh_token = os.getenv("STRAVA_REFRESH_TOKEN")
strava_code = os.getenv("STRAVA_CODE")

url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"


def get_authorization_code():

    post_data = {
    "client_id": client_id,
    "client_secret": client_secret,
    "code": strava_code, 
    "grant_type": "authorization_code"
    }

    post_response = requests.post(url, data=post_data)
    print(post_response)
    token = post_response["code"]

    return post_response

def get_refresh_token():
    
    post_data = {
    "client_id": client_id,
    "client_secret": client_secret,
    "refresh_token": refresh_token,
    "grant_type": "refresh_token"
    }

    post_response = requests.post(url, data=post_data)
    token = post_response.json()["access_token"]
    print(post_response.json())

    return token

refresh_token = get_refresh_token()
header = {'Authorization': 'Bearer ' + refresh_token}
parameters = {'per_page': 200, 'page': 1}

my_dataset = requests.get(activites_url, headers=header, params=parameters).json()

print(my_dataset[0]["name"])
print(my_dataset[0]["map"]["summary_polyline"])
