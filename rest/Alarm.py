import RPi.GPIO as GPIO

class Alarm(object):
    def __init__(self):
        self.led = 20
        self.sirene = 16
        self.sensor = 21

    def on(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup( self.led, GPIO.OUT)
        GPIO.setup( self.sensor, GPIO.IN) 
        GPIO.setup( self.sirene, GPIO.OUT)
        self.removeEventDetectorOnSensor()
        GPIO.add_event_detect( self.sensor , GPIO.RISING, callback=self.alarmOn)  

    def off(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup( self.led, GPIO.OUT)
        GPIO.setup( self.sensor, GPIO.IN) 
        GPIO.setup( self.sirene, GPIO.OUT)
        self.alarmOff()
        self.cleanAllPins()

    def turnAlarmOff(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup( self.led, GPIO.OUT)
        GPIO.setup( self.sirene, GPIO.OUT)
        self.alarmOff()

    def removeEventDetectorOnSensor(self):
        GPIO.remove_event_detect(self.sensor)

    def alarmOn(self, channel):
        GPIO.output(self.sirene, True)
        GPIO.output(self.led, True)

    def alarmOff(self):
        GPIO.output(self.sirene, False)
        GPIO.output(self.led, False)

    def cleanAllPins(self):
        GPIO.cleanup(self.led)
        GPIO.cleanup(self.sirene)
        GPIO.cleanup(self.sensor)


