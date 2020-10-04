from picamera import PiCamera
from time import sleep
import datetime

basename = "smr"
suffix = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.jpg'
filename = "_".join([basename, suffix])
print(filename)

camera = PiCamera()

camera.resolution = (640, 480)
camera.start_preview()

camera.annotate_text = "Smart CCTV"
camera.annotate_text_size=20
sleep(5)

camera.capture('/home/pi/captureImages/'+filename)
camera.stop_preview()
