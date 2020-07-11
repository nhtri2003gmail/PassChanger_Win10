MyAddr = 'username@gmail.com'
MyPass = 'password'
ToAddr = 'username@gmail.com'

########################################################

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def SendMail():
    ## Setup SMTP server
    s=smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MyAddr, MyPass)

    ## User Input
    print('What do you want to ask?')
    mes = input("> ")
    print(f'[+] Sending email to {ToAddr}...')
    
    ## Send mail
    msg=MIMEMultipart()

    ## Fill parameters
    msg['From']=MyAddr
    msg['To']=ToAddr
    msg['Subject']='Questions'

    ## Add message to body
    msg.attach(MIMEText(mes, "plain"))

    ## Send mail
    s.send_message(msg)

    del msg
    s.close()
    print("[+] Successfully sent email!")
    print('------------------------------------------------------------------')
    print('[+] He might be busy at the moment, please wait or try again later')
    print("[+] Waiting for his reply...")

########################################################

import imaplib
import email

def ReadMail(mostRecentNow):
    ## Set up server
    mail = imaplib.IMAP4_SSL("smtp.gmail.com")

    ## Login
    mail.login(MyAddr, MyPass)

    ## Choose Inbox
    mail.select("INBOX")

    ## Fetch email
    result, data = mail.fetch(mostRecentNow, "(RFC822)")

    for item in data:
        if isinstance(item, tuple):
            msg = email.message_from_bytes(item[1])

            subject = msg['Subject']

            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    try:
                        body = part.get_payload(decode=True).decode()
                    except:
                        pass
                    if content_type=='text/plain':
                        print('\nJohnathan Huu Tri\'s reply:')
                        print(f'\nSubject: {subject}')
                        print('Body:')
                        print(body)
    mail.close()
    mail.logout()
                    
########################################################

import imaplib

def CountMail():
    ## Set up server
    mail = imaplib.IMAP4_SSL("smtp.gmail.com")

    ## Login
    mail.login(MyAddr, MyPass)

    ## Choose Inbox
    mail.select("INBOX")

    ## Get emails
    result, data = mail.search(None, "ALL")
    inboxItem = data[0].split()

    ## Get the latest email id
    mostRecent = inboxItem[-1]

    ## Count the number of emails at the moment
    c = len(inboxItem)
    
    return c, mostRecent

########################################################

import time
from datetime import datetime

if __name__=='__main__':
    print('[+] Welcome to the communication with Johnathan Huu Tri via Email!')
    print(f'[+] Your current email adress is {MyAddr}!')
    c, mostRecent = CountMail()
    mostRecent = mostRecent.decode()

    while(True):
##        SendMail()
        print()
        
        cNow, mostRecentNow = CountMail()
        while(cNow<=c and mostRecentNow.decode()<=mostRecent):
            cNow, mostRecentNow = CountMail()
            tNow = str(datetime.now().time())
            print(f'\rUpdated at {tNow}', end='')
            time.sleep(1)
        
        ReadMail(mostRecentNow)
        c, mostRecent = CountMail()
        mostRecent = mostRecent.decode()
