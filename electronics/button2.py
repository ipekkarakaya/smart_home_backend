import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(23, GPIO.OUT)  #LED to GPIO14

def changeLed(channel):
    if (GPIO.input(23) == True):
        GPIO.output(23, False)
    else:
        GPIO.output(23, True)

try:
    GPIO.add_event_detect(11, GPIO.BOTH, callback=changeLed, bouncetime=300)
    while 1:
        time.sleep(2)

except KeyboardInterrupt:
  print('ENDE')

finally:
  GPIO.cleanup()
