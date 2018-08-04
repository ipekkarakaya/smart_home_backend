### https://www.youtube.com/watch?v=_ACe6z-Hp2E 
### https://www.youtube.com/watch?v=Zv5AtEADfZ0

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 27
sirene = 24
sensor = 25

GPIO.setup(led, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN) 
GPIO.setup(sirene, GPIO.OUT)  

def alaaarm(channel):
  print('ALARM!!!')
  GPIO.output(sirene, True)
  GPIO.output(led, True)
  time.sleep(5)
  GPIO.output(sirene, False)
  GPIO.output(led, False)

try:
  GPIO.add_event_detect(sensor , GPIO.RISING, callback=alaaarm)
  while True:
    time.sleep(1)
         
except KeyboardInterrupt:
  print('ENDE')

finally:
  GPIO.cleanup()
