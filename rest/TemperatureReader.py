import Adafruit_DHT

class TemperatureReader(object):
    def __init__(self):
        self.sensorPin = 4
        self.sensor = Adafruit_DHT.DHT11

    def readTemperature(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.sensorPin)
        str_temp = ' {0:0.2f} *C '.format(temperature)
        return str_temp