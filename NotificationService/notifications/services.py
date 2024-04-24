import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_SENDER = 'duohealth0@gmail.com'
EMAIL_PASSWORD = 'gxopinvriohdwyzd'

def send_email_notification(user_email, subject, body):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:           # Create a secure SSL context
        smtp.ehlo()                                             # Identify yourself to an ESMTP server using EHLO
        smtp.starttls()                                         # Put the SMTP connection in TLS (Transport Layer Security) mode
        smtp.ehlo()                                             # Re-identify yourself to an ESMTP server using EHLO

        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)                # Log in on an SMTP server that requires authentication

        #subject = 'MiniStackOverflow response'                # Define the subject and body of the email

        msg = f'Subject: {subject}\n\n{body}'                   # Format the message   

        smtp.sendmail(EMAIL_SENDER, user_email, msg)   
