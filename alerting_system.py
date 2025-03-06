#!/usr/local/bin/python3
import smtplib

def send_email_alert(subject, body):
    sender_email = 'sender-email-address'
    receiver_email = 'receiver-email-address'
    password = 'password'
    message = f'Subject: {subject}\n\n{body}'
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)