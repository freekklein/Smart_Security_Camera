from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.vflip = True
camera.start_preview(alpha=192)
sleep(2)
camera.capture('/home/pi/Desktop/pic.jpg')
camera.stop_preview()
