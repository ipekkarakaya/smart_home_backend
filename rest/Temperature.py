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

        self.display = Adafruit_SSD1306.SSD1306_128_64(rest=self.RST, i2c_address=0x3C)
        
        self.display.begin()
        self.display.clear()
        self.display.display()

        self.displayWidth = self.display.width
        self.displayHeight = self.display.height
        self.image = Image.new('1', (self.displayWidth, self.displayHeight))
        self.draw = ImageDraw.Draw(self.image)
        self.draw.rectangle((0,0,self.displayWidth,self.displayHeight), outline=0, fill=0)        

        self.font = ImageFont.truetype('Roboto-Medium.ttf', 36)

        buttonPin = 27

        GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(buttonPin, GPIO.BOTH, callback=self.writeTemperatureOnDisplay, bouncetime=300)

    def prepareDisplay(self):
        self.display = Adafruit_SSD1306.SSD1306_128_64(rest=self.RST, i2c_address=0x3C)
        
        self.display.begin()
        self.display.clear()
        self.display.display()

        self.displayWidth = self.display.width
        self.displayHeight = self.display.height
        self.image = Image.new('1', (self.displayWidth, self.displayHeight))
        self.draw = ImageDraw.Draw(self.image)
        self.draw.rectangle((0,0,self.displayWidth,self.displayHeight), outline=0, fill=0)        

        self.font = ImageFont.truetype('Roboto-Medium.ttf', 36)

    def readTemperature(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.sensorPin)
        temperatureAsString = ' {0:0.2f} *C '.format(temperature)
        return temperatureAsString

    def showTemperatureOnDisplay(self):
        test = ""

    def writeTemperatureOnDisplay(self, channel):
        self.draw.rectangle((0,0,self.displayWidth,self.displayHeight), outline=0, fill=0)
        temperature = self.readTemperature()
        self.draw.text((5, 10),    temperature,  self.font, fill=255)
        self.display.image(self.image)
        self.display.display()
