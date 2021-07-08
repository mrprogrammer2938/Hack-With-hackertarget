#!/usr/bin/python3
# This Programm write by Mr.nope
# Hacking With Hacker Target Web 1.2.0

import os
import subprocess
import time
import sys
import requests
import platform

info = """
This code write by Mr.nope
Version: 1.2.0
"""
banner = """
  ___ ___                   __     
 /   |   \ _____     ____  |  | __ 
/    ~    \\__  \  _/ ___\ |  |/ / 
\    Y    / / __ \_\  \___ |    <  
 \___|_  / (____  / \___  >|__|_ \ 
       \/       \/      \/      \/ 
                           """
opt = "\nHack/> "
system = platform.uname()[0]

def cls():
    if system == 'Linux':
        os.system("clear")
    elif system == 'Windows':
        os.system("cls")
    else:
        print("\nPlease, Run This Programm on Windows, Linux!\n")
        sys.exit()
def main():
    os.system("printf '\033]2;Hack\a'")
    cls()
    print(banner)
    print(info)
    print("\n{1}.Port Scan")
    print("{2}.Ping Test")
    print("{3}.Whois Lookup")
    print("{4}.revers lookup")
    print("{5}.Geo IP")
    print("{99}.Exit or Ctrl + D")
    choose = input(opt)
    if choose == '1':
        portscan()
    elif choose == '2':
        pingtest()
    elif choose == '3':
        whois()
    elif choose == '4':
        rev()
    elif choose == '5':
        geoip()
    elif choose == '99':
        ext()
    else:
        main()
def try1():
    try_to_menu1 = input("\npress Enter...")
    if try_to_menu1 == '':
        main()
    else:
        main()
def try2():
    try_to_menu2 = input("\nDo you want to try again? [y/n] ")
    if try_to_menu2 == 'y':
        portscan()
    elif try_to_menu2 == 'n':
        try1()
    else:
        try2()
def geoip():
    cls()
    host = input("\nEnter host: ")
    attack_5 = requests.get("https://api.hackertarget.com/geoip/?q=" + host).text
    print(attack_5)
    try6()
def try6():
    try_to_menu_5 = input("\nDo you want to try again? [y/n] ")
    if try_to_menu_5 == 'y':
        geoip()
    elif try_to_menu_5 == 'n':
        try1()
    else:
        try6()
def whois():
    cls()
    host = input("\nEnter host: ")
    attack_3 = requests.get("https://api.hackertarget.com/whois/?q=" + host).text
    print(attack_3)
    try4()
def try4():
    try_to_menu3 = input("\nDo you want to try again? [y/n] ")
    if try_to_menu3 == 'y':
        whois()
    elif try_to_menu3 == 'n':
        try1()
    else:
        try4()
def ext():
    cls()
    print("\nExiting....")
    sys.exit()
def try5():
    try_to_menu4 = input("\nDo you want to try again? [y/n] ")
    if try_to_menu4 == 'y':
        rev()
    elif try_to_menu4 == 'n':
        try1()
    else:
        try5()
def portscan():
    cls()
    host = input("\nEnter host: ")
    attack = requests.get("https://api.hackertarget.com/nmap/?q=" + host).text
    print(attack)
    try2()
def rev():
    cls()
    host = input("\nEnter host: ")
    attack_4 = requests.get("https://api.hackertarget.com/reverseiplookup/?q=" + host).text
    print(attack_4)
    try5()
def pingtest():
    cls()
    host = input("\nEnter host: ")
    packet = input("\nEnter packet: ")
    time.sleep(2)
    attack_2 = subprocess.getoutput(f'ping -w {packet} {host}')
    print(attack_2)
    try3()
def try3():
    try_to_menu_3 = input("\nDo you want to try again? [y/n] ")
    if try_to_menu_3 == 'y':
        pingtest()
    elif try_to_menu_3 == 'n':
        try1()
    else:
        try3()
if __name__ == '__main__':
    try:
        try:
            main()
        except EOFError:
            print("\nCtrl + D")
            print("\nExiting...")
            sys.exit()
    except KeyboardInterrupt:
        print("\nCtrl + C")
        print("\nStop Hack Work !!!")
        try1()