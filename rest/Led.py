import RPi.GPIO as GPIO

class Led(object):
    def __init__(self):
        self.button = 23
        self.led = 14
        self.activateButton()

    def on(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.led,GPIO.OUT)
        GPIO.output(self.led,True)

    def off(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.led,GPIO.OUT)
        GPIO.output(self.led,False)

    def activateButton(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(led, GPIO.OUT)
        GPIO.add_event_detect(23, GPIO.RISING, callback=changeLed, bouncetime=300)

    def changeLed(self, channel):
        if (GPIO.input(led) == True):
            GPIO.output(led, False)
        else:
            GPIO.output(led, True)
