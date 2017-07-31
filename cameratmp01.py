from datetime import datetime
from picamera import PiCamera
import time

def getTime():
	return datetime.now().hour*3600 + datetime.now().minute*60 + datetime.now().second
def takePicture():
	PiCamera.start_preview()
	sleep(2)
	camera.capture_continuous('img{timestamp:%Y-%m-%d-%H-%M}.jpg')
def main():
	getTime()
	takePicture()
	time.sleep(3600)
while True:
	if getTime() <=25200 or getTime() >= 64800:
		main()

sys.exit(0)
