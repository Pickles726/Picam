from datetime import datetime
from picamera import PiCamera
import time
import os
import sys

days = {'sun': 6, 'mon': 0, 'tue': 1, 'wed': 2 , 'thu': 3, 'fri': 4, 'sat': 5} # Create day directory, and get current day

### Config variables
daysToRun = ['mon', 'tue', 'wed', 'thu', 'fri'] # List of days pictures will be taken on
startTime = 36000 # Time (in seconds) script will start taking pictures
endTime = 64800 # Time (in seconds) script will stop taking pictures
savePath = "/media/pi/pondsusb1/" # Default path to save images
intervalTime = 1800 # Interval time (in seconds) between each picture

# Returns current time
def getTime():
	return datetime.now().hour*3600 + datetime.now().minute*60 + datetime.now().second

def takePicture():
	with PiCamera() as camera:
		time.sleep(2)
		camera.resolution = (3280, 2464)
		DATE = datetime.now().strftime('%m-%d-%y_%H%M%S')
		camera.capture('%simg%s.jpg' % (savePath, DATE))

while True:
	day = datetime.today().weekday() # Get day every loop
	if any([day == days[x] for x in daysToRun]):# Checks to make sure day is in list of daysToRun
		if startTime <= getTime() <= endTime: # Runs if getTime() meets the time range of startTime and endTime
			takePicture()
		time.sleep(intervalTime)

sys.exit(0)
