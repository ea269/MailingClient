import smtplib
from email import encoders
from email.mime import text, base, multipart

# Gmail.com w/ port 587 w/ TLS
server = smtplib.SMTP('smtp.gmail.com', 587)

# Start service
server.ehlo()

# Login info 
with open('credentials.txt', 'r') as f:
    email = f.read()
    password = f.read()
    to = f.read()

# Login
server.login(email, password)

# Message headers
message = multipart.MIMEMultipart()
message['From'] = 'dad'
message['To'] = to
message['Subject'] = 'Testing 1 2 3.'

# Message body
with open('mail.txt', 'r') as f:
    mail = f.read()

# Combine them
message.attach(text.MIMEText(message, 'plain'))

# Image
filename = 'stern_dad.jpg'
attachment = open(filename, 'rb')

# Payload obj
p = base.MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())
