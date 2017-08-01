from datetime import datetime
from picamera import PiCamera
import time
import os

# Returns current time
def getTime():
	return datetime.now().hour*3600 + datetime.now().minute*60 + datetime.now().second

def takePicture():
	with PiCamera() as camera:
		time.sleep(2)
		camera.resolution = (3280, 2464)
		DATE = datetime.now().strftime('%m-%d-%y_%H%M%S')
		camera.capture('/media/pi/pondsusb/img%s.jpg' % DATE)

# Runs main() if getTime() meets the time range
while True:
	if getTime() >=25200 or getTime() <= 64800:
		takePicture()
	time.sleep(3598)

sys.exit(0)
