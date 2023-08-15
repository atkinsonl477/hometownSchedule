from operator import indexOf
from datetime import datetime, timedelta
import PyPDF2 as reader



days = ['Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu']


#grabs pdf, reads it and keeps it in a single string and a list
pdf = open('nameofSchedule', 'rb')
pdfreader = reader.PdfReader(pdf)

sched = ''
numOfPages = len(pdfreader.pages)
for i in range(numOfPages):
    sched += pdfreader.pages[i].extract_text() + '\n'

#print(sched)

schedList = sched.splitlines()




currentDate = ''
from main import addToSchedule
for item in schedList:
    if 'Employee Schedule' in item or 'Day Total' in item or 'Overall Total' in item:
        continue
    
    if item[0:3] in days and 'Hours' in item:
        currentDate = item.split(' ')[1]
        continue
    
    
    currentdatetime = currentDate.split('/')
   
    
    #print(currentDate, item)
    
    startTime = item.split(' ')[indexOf(item.split(' '), '-') - 1]
    if startTime[-1] == "p" and not startTime[0:2] == '12':
        afternoon = True
    else:
        afternoon = False
    startTime = startTime[0: -1].split(':')
    startTime[0], startTime[1] = int(startTime[0]), int(startTime[1])
    if afternoon:
        startTime[0] += 12
    
    startDate = datetime(2000 + int(currentdatetime[2]), int(currentdatetime[0]), int(currentdatetime[1]), startTime[0], startTime[1])
    hours = timedelta(hours=float(item.split()[-1]))
    
    endDate = startDate + hours
    name = ' '.join(item.split(' ')[0:indexOf(item.split(' '), '-') - 1])
    #print(name, startDate.isoformat(), '-', endDate.isoformat())
    
    addToSchedule(name, startDate, endDate)



