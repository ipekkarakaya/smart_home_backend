from flask import Flask, request, make_response, Response
from LedService import LedService
from AlarmService import AlarmService
from TemperatureReader import TemperatureReader
from TemperatureService import TemperatureService

app = Flask(__name__)

ledService = LedService()
alarmService = AlarmService()
temperatureService = TemperatureService()

defaultResponse = Response(" ", status=200)
defaultResponse.headers.set("Content-Type", "text/plain")
defaultResponse.headers.set("Access-Control-Allow-Origin", "*")

@app.route("/led/on", methods=["POST"])
def ledOn():
    ledService.on()
    return defaultResponse

@app.route("/led/off", methods=["POST"])
def ledOff():
    ledService.off()
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