from flask import Flask, request
from Led import Led

app = Flask(__name__)

led = Led()

@app.route("/Led/on", methods=["POST"])
def ledOn():
    led.on()

@app.route("/Led/off", methods=["POST"])
def ledOff():
    led.off()

if __name__ == "__main__":
    app.run(debug=True)