import Adafruit_DHT
from time import sleep
import os

import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

sensor = Adafruit_DHT.DHT1l

pin = 4


while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    str_temp = ' {0:0.2f} *C '.format(temperature)
    print("Temperatur: " + str_temp)