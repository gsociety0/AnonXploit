from colorama import Fore, Back, Style

def logo():
    logo = f"""
 /\  _  _  _ \/ _ | _ ._|_
/~~\| |(_)| |/\|_)|(_)| | 
{Style.BRIGHT + Back.BLACK + Fore.RED }  by gsociety{Style.BRIGHT + Back.BLACK + Fore.GREEN}  |
"""
    print(Style.BRIGHT + Fore.GREEN + logo + Style.RESET_ALL)
    print()