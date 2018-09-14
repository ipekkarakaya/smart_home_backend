import Adafruit_DHT
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import RPi.GPIO as GPIO
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class Temperature(object):
    def __init__(self):
        self.sensorPin = 4
        self.sensor = Adafruit_DHT.DHT11
        self.RST = 24
        self.DC = 23
        self.SPI_PORT = 0
        self.SPI_DEVICE = 0

    def prepareDisplay(self):
        disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)
        
        disp.begin()
        disp.clear()
        disp.display()

        width = disp.width
        height = disp.height
        image = Image.new('1', (width, height))

        self.draw = ImageDraw.Draw(image)

        self.padding = 2
        shape_width = 20
        top = padding
        bottom = height-padding

        x = padding

        self.fontSmall = ImageFont.truetype('cac_champagne.ttf', 18)
        self.fontNormal = ImageFont.truetype('cac_champagne.ttf', 20)
        self.fontBig = ImageFont.truetype('cac_champagne.ttf', 24)

    def readTemperature(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.sensorPin)
        temperatureAsString = ' {0:0.2f} *C '.format(temperature)
        return temperatureAsString

    def showTemperatureOnDisplay(self):
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        test = ""

    def writeTemperatureOnDisplay(self, channel):
