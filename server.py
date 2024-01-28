import os 
from logo import logo 
from colorama import Fore ,Style 
from time import sleep 
def main ():
    os .system ("clear")
    logo ()
    O00000O0O0000O0O0 =input (Style .BRIGHT +Fore .GREEN +"["+Style .NORMAL +Fore .YELLOW +"?"+Style .BRIGHT +Fore .GREEN +"]"+" RAT Name to Listen: "+Fore .WHITE )
    os .system ("clear")
    logo ()
    print (Fore .WHITE +"Due to incompatibility issues on the part of metasploit framework, some features were"+Fore .RED +" disabled"+Fore .WHITE +". Use "+Fore .YELLOW +"help"+Fore .WHITE +"."+Style .RESET_ALL )
    print ()
    sleep (3 )
    os .system (f"msfconsole -r ./DAT/{O00000O0O0000O0O0}.dat")
if __name__ =="__main__":
    main ()
