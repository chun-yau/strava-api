import requests
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("STRAVA_CLIENT_ID")
client_secret = os.getenv("STRAVA_CLIENT_SECRET")
refresh_token = os.getenv("STRAVA_REFRESH_TOKEN")

