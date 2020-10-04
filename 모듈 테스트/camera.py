from picamera import PiCamera
from time import sleep

def cam():
	camera = PiCamera()
	
	camera.start_preview()
	sleep(2)
	camera.capture('/home/pi/image.jpg')
	camera.stop_preview()

def stream():
	camera = PiCamera()

	camera.start_preview()
	sleep(2)
	camera.start_recording('/home/pi/vid.h264')
	sleep(10)
	camera.stop_recording()
	camera.stop_preview()
	
stream()
