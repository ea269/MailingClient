# MailingClient

## What this project does.
1. Connects securely to Gmail's SMTP server with TLS
2. Logs in with credential stored in a seperate file 
3. Builds a MIME message with headers and reads body from a file
4. Sends the email, and closes connection

## What I learned.
- **Python standard libraries**: using `smtplib`, `email.mime`, and `encoders`
- **File I/0**: reading credentails and contents from files
- **Network Basics**: How SMTP works and its ports
- **Security**: TLS vs SSL, importance of connections and avoiding hardcoded passwords.

## How to Run.
- Save credentails in `credentails.txt` (oner per line: email, password, recepient)
- Write message in `mail.txt`
- Run script: `python main.py`
