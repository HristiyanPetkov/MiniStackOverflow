import smtplib
import os
from dotenv import load_dotenv
from datetime import datetime

def send_email_notification(user_email, subject, body):
    try:
        load_dotenv()

        email_sender = os.getenv('EMAIL_SENDER')
        email_password = os.getenv('EMAIL_PASSWORD')

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(email_sender, email_password)

            subject = f'{subject} - {datetime.now().strftime("%H:%M:%S %d-%m-%Y")}'

            msg = f'Subject: {subject}\n\n{body}'

            smtp.sendmail(email_sender, user_email, msg)
        
        return True, None
    except Exception as e:
        return False, str(e)
