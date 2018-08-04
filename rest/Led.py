import RPi.GPIO as GPIO

class Led(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(14,GPIO.OUT)

    def on(self):
        GPIO.output(14,True)

    def off(self):
        GPIO.output(14,False)
        GPIO.cleanup(14)
