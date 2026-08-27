# Blink an LED, written by John David Villarreal 08/25/26
# Wiring:
# 	GPIO 26 -> Wire -> Resistor -> LED Pos. End
#	GND -> Wire -> LED Neg. End

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# Broadcom system on a Chip Channel, refer to docs about which pin is pin 26
GPIO.setup(26, GPIO.OUT)

# Repeat indefinetly until the program is stopped
while(1 == 1):
    # Turn the LED on
    GPIO.output(26, 1)
    time.sleep(1)
    
    #Turn the LED off
    GPIO.output(26, 0)
    time.sleep(1)