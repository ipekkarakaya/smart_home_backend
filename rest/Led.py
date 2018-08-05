import RPi.GPIO as GPIO

class Led(object):
    def __init__(self):
        self.button = 23
        self.led = 14

    def on(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.led,GPIO.OUT)
        GPIO.output(self.led,True)

    def off(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.led,GPIO.OUT)
        GPIO.output(self.led,False)
        GPIO.cleanup(self.led)
