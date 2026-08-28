# Keyboard based motor control, written by John David Villarreal 08/27/26
# The reason the keyboard is being used is to have greater control on testing the motor

import RPi.GPIO as GPIO
import time
from evdev import InputDevice, categorize, ecodes

# Setup GPIO Pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# Broadcom system on a Chip Channel, refer to docs about which pin is pin 26
GPIO.setup(26, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

# Setup keyboard to be used
dev = InputDevice('/dev/input/by-id/usb-SONiX_AMAZON_MD005_Wired_Keyboard-event-kbd')
print(dev)
# To double check the keyboard, run "ls -l /dev/input/by-id" in the terminal

# Instantiate all motor pins to control them easier later in the program
pin26 = 0
pin6 = 0

# Use keys to control motors
while(True):
    
    for event in dev.read_loop():
        if event.type == ecodes.EV_KEY:
            key_event = categorize(event)

            if key_event.keystate == key_event.key_down:
                key = key_event.keycode

                if key == 'KEY_ESC':
                    # Turn off all motors
                    print("Escape Key, turning off all motors")
                    pin26 = 0
                    pin6 = 0
                    GPIO.output(26, pin26)
                    GPIO.output(6, pin6)
                elif key == 'KEY_A':
                    # Turn Pin 26 on/off
                    pin26 = 1 - pin26
                    print(f"Key A, Changing pin 26 to {pin26}")
                    GPIO.output(26, pin26)
                elif key == 'KEY_S':
                    # Turn Pin 6 on/off
                    pin6 = 1 - pin6
                    print(f"Key S, Changing pin 6 to {pin6}")
                    GPIO.output(6, pin6)

