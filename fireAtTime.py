# fireAtTime.py, created by John David Villarreal 09/09/26
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

ON_PULSE = 0.5 # Time on per period in Seconds
OFF_PULSE = 0.5 # Time off per period in seconds
N_PERIODS = 20 # Number of periods
LOG_FILE = "/home/epilepsy_emotion/Documents/programs/epilepsy_emotion/gpio_pulse.log"

logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s: %(message)s"
        )

def main():

    logging.info("Pulsing GPIO Pins")
    
    try:

        for i in range(N_PERIODS):
            
            # Turn on Motors
            GPIO.output(26, 1)
            GPIO.output(16, 1)
            GPIO.output(6, 1)
            logging.info(f"On pulse {i+1} out of {N_PERIODS} complete")
            time.sleep(ON_PULSE)
            
            # Turn off Motors
            GPIO.output(26, 0)
            GPIO.output(16, 0)
            GPIO.output(6, 0)
            logging.info(f"Off pulse {i+1} out of {N_PERIODS} complete")
            time.sleep(OFF_PULSE)

    finally:
        GPIO.output(26, 0)
        GPIO.output(16, 0)
        GPIO.output(6, 0)
    
    logging.info(f"{N_PERIODS} of pulses complete")

if __name__ == "__main__":
    main()
