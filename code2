import RPi.GPIO as GPIO
import time
import smtplib
from email.mime.text import MIMEText

# ----------------------
# Email configuration
EMAIL_SENDER = "2051446326@qq.com"
EMAIL_PASSWORD = "qnxvzxivakuvcadg"
EMAIL_RECEIVER = "2051446326@qq.com"

SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 587
# ----------------------

# GPIO setup
MOISTURE_PIN = 17  # Adjust to match your wiring
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOISTURE_PIN, GPIO.IN)

# Email sending function
def send_email():
    subject = "Plant Watering Alert"
    body = "Soil moisture is low. Please water your plant."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
            print("Email sent successfully.")
    except Exception:
        return  # Silently ignore send errors

# Main loop
def monitor_soil():
    print("Starting soil moisture monitoring...")
    email_sent = False

    while True:
        if GPIO.input(MOISTURE_PIN) == GPIO.HIGH:
            print("Low moisture detected.")
            if not email_sent:
                print("Sending alert...")
                send_email()
                email_sent = True
            else:
                print("Alert already sent. Waiting for moisture to recover.")
        else:
            print("Moisture level is sufficient.")
            email_sent = False  # Reset flag when moisture returns

        time.sleep(10)

# Program entry point
try:
    monitor_soil()
except KeyboardInterrupt:
    print("Program terminated.")
    GPIO.cleanup()
import RPi.GPIO as GPIO
import time
import smtplib
from email.mime.text import MIMEText

# ----------------------
# Email configuration
EMAIL_SENDER = "2051446326@qq.com"
EMAIL_PASSWORD = "qnxvzxivakuvcadg"
EMAIL_RECEIVER = "2051446326@qq.com"

SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 587
# ---------------
