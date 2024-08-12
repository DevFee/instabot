import time
import os
import json
from colorama import Fore, Style
from colorama import just_fix_windows_console
from create import create_bots
from utils import change_options  # Atualize a importação
from getfs import get_followers

# Config
just_fix_windows_console()

def main():
    while True:
        os.system('cls')
        banner = """
██╗███╗   ██╗███████╗████████╗ █████╗ ██████╗  ██████╗ ████████╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝
██║██╔██╗ ██║███████╗   ██║   ███████║██████╔╝██║   ██║   ██║   
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██╔══██╗██║   ██║   ██║   
██║██║ ╚████║███████║   ██║   ██║  ██║██████╔╝╚██████╔╝   ██║   
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═╝ """
        version = "version: 0.1\t\t\t\t credits: @pqpfye\n"

        # Control variables
        with open("options.json", "r") as file:
            data = json.load(file)
        sbs = data["show_banner_spd"]
        wss = data["show_words_spd"]



        if data["flush_effect"]:
            for char in banner:
                print(Fore.GREEN + char, end="", flush=True)
                time.sleep(sbs)
            
            print(Style.RESET_ALL)  # Reseta o estilo após imprimir o banner
            
            for char in version:
                print(Fore.WHITE + char, end="", flush=True)
                time.sleep(wss)
        else:
            print(Fore.GREEN + banner)
            print(Fore.WHITE + version)
        time.sleep(0.5)
        print(Fore.YELLOW + "=================== [ Main ] ===================\n[1] - Create bots\n[2] - Get Followers\n[3] - Options\n[4] - Exit\n================================================\n")
        action = int(input(Fore.GREEN + "Choose option > "))

        match action:
            case 1:
                os.system("cls")
                print("Type amount of bots")
                print("\n+===============+\n| min: 10\t|\n| max: 100\t|\n+===============+\n")
                time.sleep(1)
                amount = int(input("> "))
                if 10 <= amount <= 100:
                    create_bots(amount)
                else:
                    text = (Fore.RED + "Invalid amount. Must be between 10 and 100.")
                    if data["flush_effect"]:
                        for char in text:
                            print(char, end="", flush=True)
                            time.sleep(wss)
                    else:
                        print(Fore.RED + "Invalid amount. Must be between 10 and 100.")
            case 2:
                text = (Fore.RED + "Insert Amount of followers")
                if data["flush_effect"]:
                    for char in text:
                        print(char, end="", flush=True)
                        time.sleep(wss)
                else:
                    print(text)
            case 3:
                change_options()
            case 4:
                text = (Fore.WHITE + "\nExiting...")
                if data["flush_effect"]:
                    for char in text:
                        print(char, end="", flush=True)
                        time.sleep(wss)
                    break
                else:
                    print(text)
                    break
            case _:
                print(Fore.RED + "\nInvalid option. Please try again.")
                print(Fore.WHITE)
try:
    main()
except Exception as e:
    print(Fore.WHITE + f"\nAn error occurred: {str(e)}\nExiting...")
