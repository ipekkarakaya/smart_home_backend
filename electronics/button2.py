import RPi.GPIO as GPIO
import time


GPIO.cleanup()

ledIsOn = False

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN)#Button to GPIO23
GPIO.setup(14, GPIO.OUT)  #LED to GPIO14

def changeLed(channel):
    GPIO.output(14, True)
    time.sleep(0.2)
    GPIO.output(14, False)
    # if ledIsOn == False:
    #     GPIO.output(14, True)
    #     ledIsOn = True
    # else:
    #     GPIO.output(14, False)
    #     ledIsOn = False
    
    time.sleep(0.1)

GPIO.output(14, False)
GPIO.add_event_detect(23, GPIO.FALLING, callback=changeLed, bouncetime=200)

while 1:
    time.sleep(2)