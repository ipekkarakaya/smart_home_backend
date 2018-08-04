import RPi.GPIO as GPIO

class Led(object):
    def __init__(self):
        pass

    def on(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(14,GPIO.OUT)
        GPIO.output(14,True)

    def off(self):
        GPIO.output(14,False)
        GPIO.cleanup(14)
