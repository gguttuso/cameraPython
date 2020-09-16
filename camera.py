from picamera import PiCamera
from time import sleep
from gpiozero import Button
import datetime

button = Button(17)
camera = PiCamera()

camera.start_preview()
frame = 1
x = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
while True:
    try:
        button.wait_for_press()
        camera.start_preview()
        sleep(2)
        camera.annotate_text = x
        camera.capture('/home/pi/Desktop/homework/frame%03d.jpg' % frame)
        frame += 1
    except KeyboardInterrupt:
        camera.stop_preview()
        break
