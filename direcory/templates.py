from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path

# to replace parameter in templates you have to import templates class
from string import Template

import smtplib

templates = Template(Path("workingwithtemplates.html").read_text())

message = MIMEMultipart()

message["from"] = "Azhar Uddin"
message["to"] = "azharsheikh760@gmail.com"
message["subject"] = "This is a test for sending emails"

params = templates.substitute({"name": "Azhar"})
message.attach(MIMEText(params, "html"))
message.attach(MIMEImage(Path("azhar.jpg").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:

    smtp.ehlo()
    smtp.starttls()
    smtp.login("azharsheikh760@gmail.com", password="Valar123@")
    smtp.send_message(message)
    print("msg sent...")
