from datetime import datetime
from picamera import PiCamera
import time
import os
import sys

# Create day directory, and get current day
days = {'sun': 6, 'mon': 0, 'tue': 1, 'wed': 2 , 'thu': 3, 'fri': 4, 'sat': 5}
day = datetime.today().weekday()

# Returns current time
def getTime():
	return datetime.now().hour*3600 + datetime.now().minute*60 + datetime.now().second

def takePicture():
	with PiCamera() as camera:
		time.sleep(2)
		camera.resolution = (3280, 2464)
		DATE = datetime.now().strftime('%m-%d-%y_%H%M%S')
		camera.capture('/media/pi/pondsusb/img%s.jpg' % DATE)

while True:
	# Checks to make sure day is not Sunday or Saturday
	if day != days['sun'] and day != days['sat']:
		# Runs if getTime() meets the time range of X and Y
		if getTime() >= 25200 and getTime() <= 64800:
			takePicture()
		time.sleep(30)

sys.exit(0)
