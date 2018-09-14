import RPi.GPIO as GPIO

class LedService1(object):
    def __init__(self):
        self.button = 19
        self.led = 26
        self.activateButton()

    def on(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.led,GPIO.OUT)
        GPIO.output(self.led,True)

    def off(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.led,GPIO.OUT)
        GPIO.output(self.led,False)
    
    def changeLed(self, channel):
        if (GPIO.input(self.led) == True):
            GPIO.output(self.led, False)
        else:
            GPIO.output(self.led, True)

    def activateButton(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.led, GPIO.OUT)
        GPIO.add_event_detect(self.button, GPIO.BOTH, callback=self.changeLed, bouncetime=300)

