"""
Pre-requiste for this to work


1. Goto https://www.google.com/settings/security/lesssecureapps
Set the permissions to allow lesssecureapps.

2. Goto https://accounts.google.com/DisplayUnlockCaptcha
Confirm the Exception and continue.

"""

#!/usr/bin/env python


import smtplib

class Gmail(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.server = 'smtp.gmail.com'
        self.port = 587
        session = smtplib.SMTP(self.server, self.port)
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.email, self.password)
        self.session = session

    def send_message(self, subject, body):
        ''' This must be removed '''
        headers = [
            "From: " + self.email,
            "Subject: " + subject,
            "To: " + self.email,
            "MIME-Version: 1.0",
           "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        self.session.sendmail(
            self.email,
            self.email,
            headers + "\r\n\r\n" + body)

try:
    gm = Gmail('sender@gmail.com', 'sender_password')
    gm.send_message('Sample Email', 'hello! Blah')
    print("Email sent")
except Exception as e:
    print(e)

