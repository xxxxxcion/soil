import smtplib
from email.mime.text import MIMEText

EMAIL_SENDER = "2051446326@qq.com"
EMAIL_PASSWORD = "qnxvzxivakuvcadg"
EMAIL_RECEIVER = "2051446326@qq.com"
SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 587

def send_email():
    subject = "Test Email"
    body = "This is a test email from your Raspberry Pi."

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
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    send_email()
