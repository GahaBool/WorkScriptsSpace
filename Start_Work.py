import webbrowser
import subprocess

import time

#all urls that need opening
all_urls = [
    #open 6 page Bitrix24
    "https://etaxi.bitrix24.ru",
    "https://etaxi.bitrix24.ru",
    "https://etaxi.bitrix24.ru",
    "https://etaxi.bitrix24.ru",
    "https://etaxi.bitrix24.ru",
    "https://etaxi.bitrix24.ru",
    "https://etaxi.bitrix24.ru",
    #open work mail and telegram etc.
    "https://web.telegram.org",
    "https://mail.google.com",
    "https://app.weeek.net/ws/697310",
]

urls = [
    #open onli telegram and mail etc.
    "https://web.telegram.org",
    "https://mail.google.com",
    "https://app.weeek.net/ws/697310",
]

def open_programs():
    programs = ['C:\\IT Invent\\ITInvent', 'C:\\Users\\Tirskih.EL\\Desktop\\rms.viewer.portable\\rutview', 'C:\\Users\\Tirskih.EL\\Desktop\\адреса Winbox\\winbox64']

    for program in programs:
        subprocess.Popen([program])


def open_urls(option):
    if option == "a":
        for url in all_urls:
            webbrowser.open_new_tab(url)
            time.sleep(3)
    else:
        for url in urls:
            webbrowser.open_new_tab(url)
            time.sleep(3)


def select_optin():
    print("a:open all page for work") 
    print("b:open everything except Bitrix24")
    option = input("Select option: ").lower()
    if option == "a" or option == "b":
        open_urls(option)
    else:
        print("Error, pleace select option")


select_optin()
open_programs()