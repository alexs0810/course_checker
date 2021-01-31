import smtplib


def send_email(recipient, subject, content):
    # Connect to Gmail's Simple Mail Transfer Protocol Server, port 587
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

    print(smtpObj.ehlo())  # establish connection to the server

    print(smtpObj.starttls())  # enable encryption for the connection - puts it in TLS mode

    smtpObj.login('asaussier99@gmail.com', 'iimyjqtyhmjxrdow')  # uses application password

    smtpObj.sendmail('asaussier99@gmail.com', recipient, 'Subject:' + subject + '\n' + content)

    smtpObj.quit()
