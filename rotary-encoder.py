#!/usr/bin/python3

# use rotary encoder for volume control

#
# circuit diagram
# (capacitors are optionally)
#
#       .---------------.                      .---------------.
#       |               |                      |               |
#       |           CLK |------o---------------| GPIO 5        |
#       |               |      |               |               |
#       |           DT  |------)----o----------| GPIO 6        |
#       |               |      |    |          |               |
#       |           SW  |------)----)----------| GPIO 13       |
#       |               |      |    |          |               |
#       |           +   |------)----)----------| 5V            |
#       |               |      |    |          |               |
#       |           GND |------)----)----------| GND           |
#       |               |      |    |          |               |
#       '---------------'      |    |          '---------------'
#            KY-040            |    |              Raspberry
#                              |    |
#                             ---  ---
#                       100nF ---  --- 100nF
#                              |    |
#                              |    |
#                              |    |
#                             ===  ===
#                             GND  GND
#

import RPi.GPIO as GPIO
from ky040 import KY040
import os, time
from subprocess import check_call


def rotaryChangeCW():
   check_call("./scripts/playout_controls.sh -c=volumedown", shell=True)

def rotaryChangeCCW():
   check_call("./scripts/playout_controls.sh -c=volumeup", shell=True)

def switchPressed():
   check_call("./scripts/playout_controls.sh -c=playerpause", shell=True)


if __name__ == "__main__":

   CLOCKPIN = 5
   DATAPIN = 6
   SWITCHPIN = 13

   GPIO.setmode(GPIO.BCM)

   ky040 = KY040(CLOCKPIN, DATAPIN, SWITCHPIN, rotaryChangeCW, rotaryChangeCCW, switchPressed)

   ky040.start()

   try:
      while True:
         time.sleep(0.2)
   finally:
      ky040.stop()
      GPIO.cleanup()






