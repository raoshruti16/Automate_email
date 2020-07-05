# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 01:08:58 2020

@author: shruti
"""

import smtplib
import config

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, config.SEND_TO, message) 
        #sendmail(from, to , (sub, mgs))
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")
        
subject = "this is a sample mail"
msg = "hello, this is me"  
send_email(subject, msg)