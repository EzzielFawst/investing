import os
import smtplib
from email.message import EmailMessage

email_user = 'bttierradelsur@gmail.com'
email_password = 'Sesshomaru'
email_send = 'ezidra39@gmail.com'

msg = EmailMessage()
msg['Subject'] = 'DB'
msg['From'] = email_user
msg['To'] = email_send

files = ['invest.db', 'investAL30.py', 'investDAIARS.py', 'investAL30D.py', 'invest.py', 'html.py', 'investDAIUSD.py', 'mail.py', 'create_invest_table.py']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_user, email_password)
    smtp.send_message(msg)
