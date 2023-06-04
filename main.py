import platform
from os import system, path
from colorama import Fore

R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
D = Fore.RESET
M = Fore.MAGENTA

def os_type():
    if platform.system() == "Windows":
        opener_win32()
    elif platform.system() == "Linux" or "Darwin":
        opener_unix()

def opener_win32():
    system('cls')
    print(Y + """ Opener on Windows """ + D + """
    WHAT DO YOU WHANT TO RUN
    1. NOTEPAD
    2. CHROME
    3. FILE EXPLORER
    4. EXIT
    """)
    try:
        selector = int(input("--> "+ M))

        if selector == 1:
            print(D)
            system("notepad.exe")
            exit
        elif selector == 2:
            print(D)
            system("start chrome.exe")
            exit
        elif selector == 3:
            print(D)
            system("explorer")
            exit
        elif selector == 4:
            print(D)
            print("bye")
            exit
        else:
            print("this option is not detected\nrun the script again")
            exit
    except ValueError:
        print(R + "the string format doenst enabled")
        print(D)

def opener_unix():
    system('clear')
    print(Y + """ Opener on linux/darwin """ + D + """
    WHAT DO YOU WHANT TO RUN
    1. FIREFOX
    2. EXIT
    """)
    try:
        selector = int(input("--> "+ M))

        if selector == 1 and path.exists("/usr/bin/firefox" or "/snap/bin/firefox" or "/bin/firefox"):
            system('firefox &')
        elif selector == 2:
            print(D)
            print("bye")
            exit
    except ValueError:
        print(R + "the string format doenst enabled")
        print(D)
            
os_type()