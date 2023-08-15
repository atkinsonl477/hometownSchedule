import os
from google.oauth2.credentials import Credentials
from datetime import datetime
SCOPES = ['https://www.googleapis.com/auth/calendar']
def checkToken():
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not creds.valid:
            os.remove("token.json")


