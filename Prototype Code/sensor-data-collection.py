import RPi.GPIO as GPIO
import time

# Set GPIO mode and pin for the motion sensor
GPIO.setmode(GPIO.BOARD)
motion_pin = 11
GPIO.setup(motion_pin, GPIO.IN)

# Function to read motion sensor data
def read_motion_sensor():
    try:
        while True:
            if GPIO.input(motion_pin):
                print("Motion detected")
            else:
                print("No motion detected")
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()

# Call the function to start data collection
read_motion_sensor()