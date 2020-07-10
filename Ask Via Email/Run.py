import smtplib
import time

MyAddr = 'emailsender@gmail.com'        # Email Sender
MyPass = 'emailsenderpassword'          # Password Sender                                 
ToAddr = 'emailreceiver@gmail.com'      # Email Receiver

########################################################

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
from email.parser import Parser
from email._policybase import compat32

def ReadMail(mostRecentNow):
    ## Set up server
    mail = imaplib.IMAP4_SSL("smtp.gmail.com")

    ## Login
    mail.login(MyAddr, MyPass)

    ## Choose Inbox
    mail.select("INBOX")

    ## Fetch email
    result, data = mail.uid('fetch', mostRecentNow, "(RFC822)")
    print(data[0][1])
    
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
    result, data = mail.uid('search', None, "ALL")
    inboxItem = data[0].split()

    ## Get the latest email id
    mostRecent = inboxItem[-1]

    ## Count the number of emails at the moment
    c = len(inboxItem)
    
    return c, mostRecent

if __name__=='__main__':
    print('[+] Welcome to the communication with Johnathan Huu Tri via Email!')
    print(f'[+] Your current email adress is {MyAddr}!')
    c, mostRecent = CountMail()
    print(c, " ", mostRecent)
    mostRecent = mostRecent.decode()
    
##    SendMail()

    cNow, mostRecentNow = CountMail()
    print(cNow, " ", mostRecentNow)
    while(c<=cNow and mostRecent<=mostRecentNow.decode()):
        cNow, mostRecentNow = CountMail()
        ReadMail(mostRecentNow)
        time.sleep(1)
