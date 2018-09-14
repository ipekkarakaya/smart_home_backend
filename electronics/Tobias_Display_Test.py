import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

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
#draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = 2
shape_width = 20
top = padding
bottom = height-padding

x = padding

font = ImageFont.load_default()
font18 = ImageFont.truetype('Minecraftia.ttf', 18)
font20 = ImageFont.truetype('Minecraftia.ttf', 20)
font24 = ImageFont.truetype('Minecraftia.ttf', 24)

draw.text((x, top),    'Joe Mama',  font=font18, fill=255)
# draw.text((x, top+18), 'DHTxx', font=font24, fill=255)

disp.image(image)
disp.display()
