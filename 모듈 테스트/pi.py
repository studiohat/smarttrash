from picamera import PiCamera
import RPi.GPIO as GPIO
import time
from time import sleep

pin = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN)


while True:
	if not GPIO.input(23):
		"""
		camera = PiCamera()
		camera.start_preview()
		sleep(2)
		camera.capture('/home/pi/image.jpg')
		camera.stop_preview()
		"""
		print("finish")
		time.sleep(1)
		#break
    
try: 
    while True:
        time.sleep(1)

except KeyboardInterrupt:
        GPIO.cleanup()
