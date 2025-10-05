import smtplib
from email import encoders
from email.mime import text, base, multipart

# Gmail.com w/ port 587 w/ TLS
server = smtplib.SMTP('smtp.gmail.com', 587)

# Start service
server.starttls()

# Login info 
with open('credentials.txt', 'r') as f:
    lines = f.readlines()
    email = lines[0].strip()
    password = lines[1].strip()
    to = lines[2].strip()

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

# Encode 
encoders.encode_base64(p)
p.add_headers('Content-Disposition', f'attachment; filename={filename}')
message.attach(p)

# Convert to string
text = msg.as_string()
server.sendmail(email, to, text)
