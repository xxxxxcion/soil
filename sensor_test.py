import RPi.GPIO as GPIO
import time

MOISTURE_PIN = 17  # Change if needed

GPIO.setmode(GPIO.BCM)
GPIO.setup(MOISTURE_PIN, GPIO.IN)

try:
    print("Starting soil moisture sensor test...")
    while True:
        value = GPIO.input(MOISTURE_PIN)
        if value == GPIO.HIGH:
            print("Soil is DRY")
        else:
            print("Soil is WET")
        time.sleep(1)
except KeyboardInterrupt:
    print("Test stopped.")
    GPIO.cleanup()
