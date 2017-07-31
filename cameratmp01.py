from datetime import datetime
from picamera import PiCamera
import time

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
		camera.capture('img%s.jpg' % DATE)

def main():
	takePicture()
	time.sleep(30)

# Runs main() if getTime() meets the time range
while True:
	if getTime() <=25200 or getTime() >= 64800:
		main()

sys.exit(0)
