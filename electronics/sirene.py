import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

sirene = 24
GPIO.setup(sirene, GPIO.OUT)

try: 
  while True:
    GPIO.output(sirene,True)
    time.sleep(5)
    GPIO.output(sirene,False)
    time.sleep(5)

except KeyboardInterrupt:
  print "ENDE"

finally:
  GPIO.cleanup()
