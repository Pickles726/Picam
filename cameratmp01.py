from datetime import datetime
from picamera import PiCamera
import time
import os

print os.getuid()
#DATE = datetime.now().strftime('%m-%d-%y_%H%M%S')
# Returns current time
def getTime():
	return datetime.now().hour*3600 + datetime.now().minute*60 + datetime.now().second

def takePicture():
#	PiCamera().start_preview()
#	time.sleep(2)
#	PiCamera().capture('img{timestamp:%Y-%m-%d-%H-%M}.jpg')
	with PiCamera() as camera:
		DATE = datetime.now().strftime('%m-%d-%y_%H%M%S')
		camera.capture('/media/pi/pondsusb/img%s.jpg' % DATE)

#def main():
#	takePicture()
	
# Runs main() if getTime() meets the time range
while True:
	print getTime()
	if getTime() >=25200 or getTime() <= 64800:
		takePicture()
	time.sleep(10)

sys.exit(0)
