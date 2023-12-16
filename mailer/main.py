import smtplib
from dotenv import load_dotenv
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.connect('smtp.gmail.com', 587)
server.ehlo()

server.login(os.getenv('EMAIL'), os.getenv('EMAIL_PASSWORD'))


msg = MIMEMultipart()
msg['From'] = 'David'
msg['To'] = 'cqc11725@nezid.com'
msg['Subject'] = 'Just a test'
with open('message.txt', 'r') as f:
	message = f.read()

fileName = 'me.jpg'

attachment = open(fileName, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())

encoders.encode_base64(part)
part.add_header('Content-Disposition', f'attachment; filename={fileName}')
msg.attach(part)

text = msg.as_string()
server.sendmail('mckinz147@gmail.com', 'cqc11725@nezid.com', text)
