#!/usr/bin/python3

import time
from colorama import Fore

try: 
    banner = (Fore.GREEN + """

    ⠀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣀⠀
    ⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣿⡿⠛⠉⠀⠀⠀⠉⠉⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⢶⣦⡄⠀⠈⢿⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⢸⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠾⠟⠃⠀⢀⣾⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣿⣷⣤⣀⠀⠀⠀⣀⣀⠀⠀⠀⣀⣤⣾⣿⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
    ⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
⠀   ⠉⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠉⠀
    """ + Fore.RESET)

    print(banner)
    print("                       ByCebra")
    time.sleep(2)

    def isvalid(n):
        t=0
        for x,y in enumerate(reversed(n)):
            y=int(y)
            if x%2==1:
                y=y*2
            elif y>=10:
                t+=y//10+y%10
            else:
                t+=y
        else:
                t+=y
        return t%10==0

    def cardtype(n):
        a=int(n[0,1]);b=int(n[0:2])
        if b>49 and b<56:return '**MASTERCARD'
        if b==34 or b==37:return '**AMERICA EXPRESS'
        if b in [60,62,64,65]: return '**DISCOVER'
        if a==41: return '**VISA'
        return 'NONE--'

    NC="5465407274645021"

    while NC!='0':
        NC=input(Fore.CYAN + "\nIngresar Tarjeta De Credito#: " + Fore.RESET)
        if isvalid(NC)==True:
            print(FORE.GREEN + "Es Valida!, tipo:",cardtype(NC) + Fore.RESET)
        else:
            print("Invalida...")
except KeyboardInterrupt:
    print(Fore.RED + "\nSaliendo de la herramienta..." + Fore.RESET)
    time.sleep(2)
