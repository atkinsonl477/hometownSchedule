from main import addToSchedule, wipeCalendar
from datetime import datetime, timedelta
now = datetime.now()
later = now + timedelta(days=1)

wipeCalendar()