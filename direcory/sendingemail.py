# multi purpose internet extention define format of email
from email.mime.multipart import MIMEMultipart
# MIMEMultipart can send both plain text as well as html format

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path

import smtplib

message = MIMEMultipart()

message["from"] = "Azhar Uddin"
message["to"] = "azharsheikh760@gmail.com"
message["subject"] = "This is a test for sending emails"

# we have to attach body to message bcoz mime doesnot support body

# attach have parameter payload its support both text image etc
message.attach(MIMEText("body"))
message.attach(MIMEImage(Path("azhar.jpg").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    # ehlo we are saying we want to send email
    smtp.ehlo()
    smtp.starttls()
    smtp.login("azharsheikh760@gmail.com", password="Valar123@")
    smtp.send_message(message)
    print("msg sent...")
