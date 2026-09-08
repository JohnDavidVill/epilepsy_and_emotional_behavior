# fireAtTime.py, created by John David Villarreal 09/08/26
# Control Motors at a specified interval

import logging
import RPi.GPIO as GPIO
import time

# Setup GPIO Pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

ON_DURATION = 30 # Duration in Seconds
LOG_FILE = "./gpio_pulse.log"

logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s: %(message)s"
        )

def main():

    logging.info(f"Pulsing GPIOs for {ON_DURATION} seconds")
    
    try:
        # Turn on motors
        GPIO.output(26, 1)
        GPIO.output(16, 1)
        GPIO.output(6, 1)
        
        # Keep on for duration
        time.sleep(ON_DURATION)

    finally:
        GPIO.output(26, 0)
        GPIO.output(16, 0)
        GPIO.output(6, 0)
    
    logging.info("Pulse complete")

if __name__ == "__main__":
    main()
