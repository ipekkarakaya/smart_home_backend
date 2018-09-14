from flask import Flask, request, make_response, Response
from LedService1 import LedService1
from LedService2 import LedService2
from LedService3 import LedService3
from LedService4 import LedService4
from AlarmService import AlarmService
from TemperatureReader import TemperatureReader
from TemperatureService import TemperatureService

app = Flask(__name__)

ledService1 = LedService1()
ledService2 = LedService2()
ledService3 = LedService3()
ledService4 = LedService4()
alarmService = AlarmService()
temperatureService = TemperatureService()

defaultResponse = Response(" ", status=200)
defaultResponse.headers.set("Content-Type", "text/plain")
defaultResponse.headers.set("Access-Control-Allow-Origin", "*")

@app.route("/led1/on", methods=["POST"])
def led1On():
    ledService1.on()
    return defaultResponse

@app.route("/led1/off", methods=["POST"])
def led1Off():
    ledService1.off()
    return defaultResponse

@app.route("/led2/on", methods=["POST"])
def led2On():
    ledService2.on()
    return defaultResponse

@app.route("/led2/off", methods=["POST"])
def led2Off():
    ledService2.off()
    return defaultResponse    

@app.route("/led3/on", methods=["POST"])
def led3On():
    ledService3.on()
    return defaultResponse

@app.route("/led3/off", methods=["POST"])
def led3Off():
    ledService3.off()
    return defaultResponse

@app.route("/led4/on", methods=["POST"])
def led4On():
    ledService4.on()
    return defaultResponse

@app.route("/led4/off", methods=["POST"])
def led4Off():
    ledService4.off()
    return defaultResponse

@app.route("/alarm/activate", methods=["POST"])
def alarmActivate():
    alarmService.on()
    return defaultResponse

@app.route("/alarm/deactivate", methods=["POST"])
def alarmDeactivate():
    alarmService.off()
    return defaultResponse


@app.route("/alarm/off", methods=["POST"])
def alarmOff():
    alarmService.turnAlarmOff()
    return defaultResponse
    
@app.route("/temperature", methods=["GET"])
def readTemperature():
    temperature = temperatureService.readTemperatureAndWriteOnDisplay()
    response = Response(temperature, status=200)
    response.headers.set("Content-Type", "text/plain")
    response.headers.set("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)