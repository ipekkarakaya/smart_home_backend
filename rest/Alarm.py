import RPi.GPIO as GPIO

class Alarm(object):
    def __init__(self):
        self.led = 27
        self.sirene = 24
        self.sensor = 25

    def on(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup( self.led, GPIO.OUT)
        GPIO.setup( self.sensor, GPIO.IN) 
        GPIO.setup( self.sirene, GPIO.OUT)
        GPIO.add_event_detect( self.sensor , GPIO.RISING, callback=self.alarmOn)  


    def off(self):
        self.alarmOff()
        GPIO.cleanup(self.led, self.sirene, self.sensor)

    def alarmOn(self, channel):
        GPIO.output(self.sirene, True)
        GPIO.output(self.led, True)

    def alarmOff(self):
        GPIO.output(self.sirene, False)
        GPIO.output(self.led, False)