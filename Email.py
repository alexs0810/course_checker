#A script that connects to your mail server and sends an email when method is called
#Used for a gmail server

import smtplib


def send_email(recipient, subject, content):
    # Connect to Gmail's Simple Mail Transfer Protocol Server, port 587
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

    print(smtpObj.ehlo())  # establish connection to the server

    print(smtpObj.starttls())  # enable encryption for the connection - puts it in TLS mode

    smtpObj.login('your@email', 'your_password')  # uses application password

    smtpObj.sendmail('your@email', recipient, 'Subject:' + subject + '\n' + content)

    smtpObj.quit()
