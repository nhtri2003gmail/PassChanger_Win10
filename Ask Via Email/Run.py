MyAddr = 'emailsender@gmail.com'        # Email Sender
MyPass = 'emailsenderpassword'          # Password Sender
ToAddr = 'emailreceiver@gmail.com'      # Email Receiver

########################################################

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def SendMail(s):

    ## User Input
    print('What do you want to ask?')
    mes = input("> ")
    
    print(f'[+] Sending email to {ToAddr}...')
    ## Create email packet
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
    print("[+] Successfully sent email!")
    print('------------------------------------------------------------------')
    print('[+] He might be busy at the moment, please wait or try again later')
    print("[+] Waiting for his reply...")

########################################################

import email

def ReadMail(mail, mostRecentNow):
    ## Choose Inbox
    mail.select("INBOX")

    ## Fetch email
    result, data = mail.fetch(mostRecentNow, "(RFC822)")

    for item in data:
        if isinstance(item, tuple):
            msg = email.message_from_bytes(item[1])     ## Using email module

            subject = msg['Subject']

            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    try:
                        body = part.get_payload(decode=True).decode()
                    except:
                        pass
                    if content_type=='text/plain':
                        print(subject)
                        print(body)
                    
########################################################

def CountMail(mail):
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
import smtplib
import imaplib
from datetime import datetime

def Chatting():
    print('[+] Welcome to the communication with Johnathan Huu Tri via Email!')
    print(f'[+] Your current email adress is {MyAddr}!')
    print()
    
    ## Setup SMTP server
    print('[+] Setting up SMTP server...')
    s=smtplib.SMTP(host='smtp.gmail.com', port=587)     ## Using smtplib
    s.starttls()
    s.login(MyAddr, MyPass)
    print('[+] Done')

    ## Set up IMAP server
    print('[+] Setting up IMAP server...')
    mail = imaplib.IMAP4_SSL("smtp.gmail.com")          ## Using imaplib
    mail.login(MyAddr, MyPass)
    print('[+] Done\n')
    
    c, mostRecent = CountMail(mail)
    mostRecent = mostRecent.decode()

    SendMail(s)

    cNow, mostRecentNow = CountMail(mail)
    while(cNow<=c and mostRecentNow.decode()<=mostRecent):
        ## Get update with cNow and mostRecentNow
        cNow, mostRecentNow = CountMail(mail)
        
        if(not(cNow<=c and mostRecentNow.decode()<=mostRecent)):
            print('\r[+] Received!                 ')
            print('------------------------------------------------------------------')
        else:
            tNow = str(datetime.now().time())           ## Using datetime
            print(f'\r[+] Updated at {tNow}', end='')
        time.sleep(1)                               ## Using time
    
    ReadMail(mail, mostRecentNow)
    print('------------------------------------------------------------------')

    ## Closing SMTP server
    print('[+] Shuting down SMTP server')
    s.close()
    print('[+] Done')

    ## Closing IMAP server
    print('[+] Shuting down IMAP server')    
    mail.close()
    mail.logout()
    print('[+] Done')

################################################################################################################

import os

def ExeCommand():
    print("Type \"Exit\" to quit")
    while(True):
        cmd = input("> ")
        if(cmd=='Exit' or cmd=='exit'):
            os.system('cls')
            break
        os.system(cmd)

import os

if __name__=='__main__':
    while(True):
        print('1. Send email')
        print('2. Execute command')
        print('3. Exit')
        c = input("> ")
        if(c=='1'):
            Chatting()
        elif(c=='2'):
            os.system('cls')
            ExeCommand()
        elif(c=='3'):
            break
        else:
            os.system('cls')
