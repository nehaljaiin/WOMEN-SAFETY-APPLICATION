import os
import time
import smtplib
from email.mime.text import MIMEText

# Configuration
SMS_API_KEY = "YOUR_SMS_API_KEY"
EMAIL_USERNAME = "YOUR_EMAIL_USERNAME"
EMAIL_PASSWORD = "YOUR_EMAIL_PASSWORD"
RECIPIENT_EMAIL = "RECIPIENT_EMAIL_ADDRESS"
RECIPIENT_PHONE_NUMBER = "RECIPIENT_PHONE_NUMBER"

# Function to send SMS
def send_sms(message):
    url = f"https://api.smsapi.com/v2/sms.do?access_token={SMS_API_KEY}&to={RECIPIENT_PHONE_NUMBER}&message={message}"
    os.system(f"curl {url}")

# Function to send email
def send_email(message):
    msg = MIMEText(message)
    msg['Subject'] = "Women's Safety Alert"
    msg['From'] = EMAIL_USERNAME
    msg['To'] = RECIPIENT_EMAIL

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
    server.sendmail(EMAIL_USERNAME, RECIPIENT_EMAIL, msg.as_string())
    server.quit()

# Main function
def women_safety_app():
    print("Women's Safety App")
    print("----------------")

    while True:
        print("1. Send SOS Message")
        print("2. Call Emergency Services")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            message = "I am in danger. Please help me."
            send_sms(message)
            send_email(message)
            print("SOS message sent successfully!")

        elif choice == "2":
            print("Calling emergency services...")
            # Replace with your local emergency services number
            os.system("tel://911")

        elif choice == "3":
            print("Exiting app...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    women_safety_app()