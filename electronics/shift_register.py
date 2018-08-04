# 
# quelle: https://elektronik.skyline-service.de/raspberrypi/schieberegister-am-raspberrypi-anschliessen/


import RPi.GPIO as IO   # um die Pins ansteuern zu koennen, brauchen wir die Lib
import time             # fuer die Delays benoetigen wir die time-Lib
IO.setwarnings(False)   # Keine Warnungen anzeigen

IO.setmode(IO.BCM)      # Programmiermodus, um die Pins zu setzen
IO.setup(4,IO.OUT)      # Setze Pin 4 als Ausgang (SER)
IO.setup(5,IO.OUT)      # Setze Pin 5 als Ausgang (SCK)
IO.setup(6,IO.OUT)      # Setze Pin 6 als Ausgang (RCK)

while 1:                # unendliche Schleife
    for y in range(8):  # Schleife wird 8Mal (8bit) ausgefuehrt
        IO.output(4,1)  # eine 1 an den seriellen Input senden
        time.sleep(0.1) # 100ms warten
        IO.output(5,1)  # SCK-Pin auf High ziehen, damit das Register anfaengt die Bits um eine Stelle zu verschieben
        time.sleep(0.1) # 100ms warten
        IO.output(5,0)  # SCK_Pin wieder auf LOW ziehen
        IO.output(4,0)  # Das Datenpin loeschen
        IO.output(6,1)  # RCK auf HIGH setzen, damit das Register zur Ausgabe kopiert wird
        time.sleep(0.1) # 100ms warten
        IO.output(6,0)  # RCK wieder auf LOW setzen

    for y in range(8):  # Schleife wird 8Mal (8bit) ausgefuehrt
        IO.output(4,0)  # eine 0 an den seriellen Input senden
        time.sleep(0.1) # 100ms warten
        IO.output(5,1)  # SCK-Pin auf High ziehen, damit das Register anfaengt die Bits um eine Stelle zu verschieben
        time.sleep(0.1) # 100ms warten
        IO.output(5,0)  # SCK_Pin wieder auf LOW ziehen
        IO.output(4,0)  # Das Datenpin loeschen -> eine 0 senden
        IO.output(6,1)  # RCK auf HIGH setzen, damit das Register zur Ausgabe kopiert wird
        time.sleep(0.1) # 100ms warten
        IO.output(6,0)  # RCK wieder auf LOW setzen
