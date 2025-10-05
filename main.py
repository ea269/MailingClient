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

# Login
server.login(email, password)
