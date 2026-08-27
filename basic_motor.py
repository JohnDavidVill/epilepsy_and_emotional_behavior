# Basic motor control, written by John David Villarreal 08/26/26
# Motor control wire should be connected to pin 26

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# Broadcom system on a Chip Channel, refer to docs about which pin is pin 26
GPIO.setup(26, GPIO.OUT)

# Repeat indefinetly until the program is stopped
while(True):
    # Turn the motor on
    GPIO.output(26, 1)
    time.sleep(5)
    
    #Turn the motor off
    GPIO.output(26, 0)
    time.sleep(1)
