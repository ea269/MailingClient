import smtplib

# Gmail.com w/ port 456 w/ TLS
server = smtplib.SMTP('smtp.gmail.com', 456)

# Start service
server.ehlo()

# Login info 
with open('credentials.txt', 'r') as f:
    email = f.read()
    password = f.read()

# Login
server.login(email, passwrod)
