
#stuff I made
from checktoken import checkToken


import datetime
import os.path
from time import sleep

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar']
workCalendar = 'secretcalendaraddress@groups.gmail.com'


creds = None
    
checkToken()

if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        pass
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'secretfile.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

emailList = {
    'Logan Atkinson': 'slowloganatkinson@gmail.com',
    'Employee name1': 'employeemail1@gmail.com',
    'Employee name2': 'employeemail2@gmail.com'


}

def addToSchedule(name: str, startdatetime: datetime, enddatetime: datetime):
    if name in emailList:
        attendee = emailList[name]
        service = build('calendar', 'v3', credentials=creds)
        event = {
                'summary': 'Work Shift for ' + name,
                'attendees': [{
                    'email': attendee
                     }],
            
                'start': {
                    'dateTime': startdatetime.isoformat(),
                    'timeZone': 'CST6CDT'
                
            
                },
                'end': {
                    'dateTime': enddatetime.isoformat(),
                    'timeZone': 'CST6CDT'
            
                },
        }
    
        event = service.events().insert(calendarId=workCalendar, body=event).execute()
        print('Event created:', (event.get('summary'), event.get('start')))

        
    else:
        print('No email found for', name)
        sleep(.2)
        



def wipeCalendar(): #Deletes literally every event in workCalendar
    service = build('calendar', 'v3', credentials=creds)
    events_result = service.events().list(calendarId=workCalendar, timeMin=datetime.datetime(2000, 1, 1).isoformat() + 'Z',
                                              maxResults=10000, singleEvents=True,
                                              orderBy='startTime').execute()

    events = events_result.get('items', [])
    if not events:
        print('No events detected')
        return
    for event in events:
        print('deleting', event['summary'], event['start'])
        service.events().delete(calendarId=workCalendar, eventId=event['id']).execute()
    print('Finished deleting events.')
    