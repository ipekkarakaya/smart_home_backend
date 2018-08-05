import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=PUD_DOWN)#Button to GPIO23
GPIO.setup(14, GPIO.OUT)  #LED to GPIO14

def changeLed(channel):
    print"Button pressed"
    # if (GPIO.input(14) == True):
    #     GPIO.output(14, False)
    # else:
    #     GPIO.output(14, True)

try:
    GPIO.add_event_detect(23, GPIO.RISING, callback=changeLed, bouncetime=100)
    while 1:
        time.sleep(2)

except KeyboardInterrupt:
  print('ENDE')

finally:
  GPIO.cleanup()
