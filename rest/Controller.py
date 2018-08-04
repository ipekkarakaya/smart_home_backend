from flask import Flask, request
from Led import Led
from Alarm import Alarm

app = Flask(__name__)

led = Led()
alarm = Alarm()

@app.route("/Led/on", methods=["POST"])
def ledOn():
    led.on()
    return ""

@app.route("/Led/off", methods=["POST"])
def ledOff():
    led.off()
    return ""

@app.route("/alarm/activate", methods=["POST"])
def alarmActivate():
    alarm.on()
    return ""

@app.route("/alarm/deactivate", methods=["POST"])
def alarmkDeactivate():
    alarm.off()
    return ""


@app.route("/alarm/off", methods=["POST"])
def alarmkOff():
    alarm.turnAlarmOff()
    return ""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)