import RPi.GPIO as GPIO
import time


GPIO.cleanup()

ledIsOn = False

GPIO.setmode(GPIO.BCM)
def changeLed(channel):
    if ledIsOn == False:
        GPIO.output(14, True)
        ledIsOn = True
    else:
        GPIO.output(14, False)
        ledIsOn = False
    
    time.sleep(0.1)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(14, GPIO.OUT)  #LED to GPIO14

GPIO.add_event_detect(23, GPIO.RISING, callback=changeLed)

while 1:
    time.sleep(2)