import RPi.GPIO as GPIO

class Led(object):
    def __init__(self):
        self.button = 23
        self.led = 14

    def on(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(led,GPIO.OUT)
        GPIO.output(led,True)

    def off(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(led,GPIO.OUT)
        GPIO.output(led,False)
        GPIO.cleanup(led)
