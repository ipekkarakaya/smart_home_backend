import RPi.GPIO as GPIO


GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
def changeLed(channel):
    ledState = GPIO.input(14)

    if ledState == True:
        GPIO.output(14, False)
    else:
        GPIO.output(14, True)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(14, GPIO.OUT)  #LED to GPIO14

GPIO.add_event_detect(23, GPIO.RISING, callback=changeLed)

