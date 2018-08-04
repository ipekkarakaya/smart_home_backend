import RPi.GPIO as GPIO

class Led(object):
    def __init__(self):
        pass

    def on(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(26,GPIO.OUT)
        GPIO.output(26,True)

    def off(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(26,GPIO.OUT)
        GPIO.output(26,False)
        GPIO.cleanup(26)
