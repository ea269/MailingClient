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
mail = multipart.MIMEMultipart()
mail['From'] = 'dad'
mail['To'] = to
mail['Subject'] = 'Testing 1 2 3.'

# Message body
with open('mail.txt', 'r') as f:
    body = f.read()

# Combine them
mail.attach(text.MIMEText(body, 'plain'))

# Image
filename = 'stern_dad.jpg'
attachment = open(filename, 'rb')

# Payload obj
p = base.MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

# Encode 
encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
mail.attach(p)

# Convert to string
text = mail.as_string()
server.sendmail(email, to, text)
