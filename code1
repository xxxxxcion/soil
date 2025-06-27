import RPi.GPIO as GPIO
import time

# Soil sensor D0 is connected to GPIO17
sensor_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)

print("Starting soil moisture monitoring... (Press Ctrl+C to stop)")

try:
    while True:
        if GPIO.input(sensor_pin) == 0:
            print("Soil is moist")
        else:
            print("Soil is dry")
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting program and cleaning up GPIO...")
    GPIO.cleanup()

