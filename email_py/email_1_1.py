#!/usr/bin/env python3

from fileinput import filename
import smtplib

'''
# server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
# server.login("example@gmail.com", "password")
# server.sendmail("example@gmail.com", "contact1@gmail.com", "hello? brother")

server = smtplib.SMTP_SSL("smtp.mail.ru", 465)
server.login("my_email@example.com", "sdasadsda")
server.sendmail("my_email@example.com", "other_mail@mail.ru", "hello? brother")

server.quit()
'''

#---------------------------------- 2 way test-------------------------------------------------
# import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP_SSL("smtp.mail.ru", 465)
with open("password.txt", "r") as f:
    password = f.read()

server.login("my_email@example.com", password)
msg = MIMEMultipart()

msg['From'] = 'my_email@example.com'
msg['To'] = 'your_email@example.com'
msg['Subject'] = 'Just a test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'coding.jpeg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)


filename = 'my_photo-1.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

html = '''\
<html>
    <head></head>
    <body>
    <a href="https://www.w3schools.com/html/html_examples.asp">Подпишись</a>
    </body
</html>
'''

msg.attach(MIMEText(html, "html"))
text = msg.as_string()
# try:
server.sendmail("my_email@example.com", "your_email@example.com", text)
# except OSError as e:
    # print(e.args)

server.quit()
