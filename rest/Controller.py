from flask import Flask, request, make_response, Response
from Led import Led
from Alarm import Alarm

app = Flask(__name__)

led = Led()
alarm = Alarm()

defaultResponse = Response(" ", status=200)
defaultResponse.headers.set("Content-Type", "text/plain")
defaultResponse.headers.set("Access-Control-Allow-Origin", "*")

@app.route("/led/on", methods=["POST"])
def ledOn():
    led.on()
    return defaultResponse

@app.route("/led/off", methods=["POST"])
def ledOff():
    led.off()
    return defaultResponse

@app.route("/alarm/activate", methods=["POST"])
def alarmActivate():
    alarm.on()
    return defaultResponse

@app.route("/alarm/deactivate", methods=["POST"])
def alarmDeactivate():
    alarm.off()
    return defaultResponse


@app.route("/alarm/off", methods=["POST"])
def alarmOff():
    alarm.turnAlarmOff()
    return defaultResponse

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)