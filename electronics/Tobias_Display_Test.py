import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import RPi.GPIO as GPIO
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)

disp.begin()

disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = 2
shape_width = 20
top = padding
bottom = height-padding

x = padding

font = ImageFont.load_default()
font18 = ImageFont.truetype('Roboto-Medium.ttf', 18)
font20 = ImageFont.truetype('Roboto-Medium.ttf', 20)
font24 = ImageFont.truetype('Roboto-Medium.ttf', 24)
font48 = ImageFont.truetype('Roboto-Medium.ttf', 48)
#draw.text((x, top),    'Joe Mama!',  font=font18, fill=255)
# draw.text((x, top+18), 'DHTxx', font=font24, fill=255)



def showText(channel):
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((50, 0),    '24.5 *C',  font=font48, fill=255)
    disp.image(image)
    disp.display()

buttonPin = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


try:
    GPIO.add_event_detect(buttonPin, GPIO.BOTH, callback=showText, bouncetime=300)
    while 1:
        time.sleep(2)

except KeyboardInterrupt:
  print('ENDE')

finally:
  GPIO.cleanup()

