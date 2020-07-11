import imaplib
import time
import email
from email.header import decode_header

username = 'username@gmail.com'
password = 'password'

########################################################

imap = imaplib.IMAP4_SSL("smtp.gmail.com")
imap.login(username, password)
status, messages = imap.select("INBOX")
status, num = imap.search(None, "ALL")
tmp = num[0].split()
mostRecent = tmp[-1]

status, data = imap.fetch(mostRecent, "(RFC822)")

for item in data:
    if isinstance(item, tuple): ## Check the first item in data
        msg = email.message_from_bytes(item[1])

        subject = msg['subject']

        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                try:
                    body = part.get_payload(decode=True).decode()
                except:
                    pass
                if content_type == 'text/plain':
                    print(body)

imap.close()
imap.logout()

        
        
