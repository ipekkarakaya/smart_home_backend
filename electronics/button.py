# 
# https://www.hackster.io/hardikrathod/push-button-with-raspberry-pi-6b6928

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(26, GPIO.OUT)  #LED to GPIO14

try:
    while True:
         button_state = GPIO.input(27)
         if button_state == False:
             GPIO.output(26, True)
             print('Button Pressed...')
             time.sleep(0.2)
         else:
             GPIO.output(26, False)
except:
    GPIO.cleanup()
