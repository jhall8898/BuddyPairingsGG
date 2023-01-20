import smtplib
import ssl
from email.message import EmailMessage
from BuddyPairing import *



toList = buddyPairing('Insert File Name')
email_sender = 'Insert Sender Email'
email_password = 'Insert Sender Email Password'
subject = 'Girl Gains at UC San Diego Buddy Pairings'
body = """
Thank you for joining our buddy pairings! We have included your buddy in this email so please reach out to them to get to know each other.  Please keep in mind that while we do our best to ensure that everyone
has a buddy that matches their preferences, not all preferences could be accommodated. We hope to fix this in the future, but we hope you have fun regardless! \n – Girl Gains at UC San Diego
"""
for index in range(len(toList)):
    email_receiver = toList[index]

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
