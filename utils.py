import json
import os
from colorama import Fore, Style
import time

# Carregar o arquivo JSON
with open("options.json", "r") as file:
    data = json.load(file)

# Global variables
wss = data["show_words_spd"]

# Change options function
def change_options():
    try:
        while True:
                os.system("cls")
                banner = """
██╗███╗   ██╗███████╗████████╗ █████╗ ██████╗  ██████╗ ████████╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝
██║██╔██╗ ██║███████╗   ██║   ███████║██████╔╝██║   ██║   ██║   
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██╔══██╗██║   ██║   ██║   
██║██║ ╚████║███████║   ██║   ██║  ██║██████╔╝╚██████╔╝   ██║   
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═╝ """
                version = "version: 0.1\t\t\t\t credits: @pqpfye\n"

                print(Fore.GREEN + banner)
                print(Fore.WHITE + version)
                time.sleep(0.5)
                print(Fore.YELLOW +"=================== [ Options ] ===================\n[1] - Flush Effect\n[2] - Banner slush speed\n[3] - Phrases flush speed\n[4] - Exit\n===================================================")
                choice = int(input(Fore.GREEN + "\nChoose option > "))
                match choice:
                    case 1:
                        os.system("cls")
                        print(Fore.YELLOW + "Type \"True\" for activate flush effect, and \"False\" for desactivate.\n")
                        value = input(Fore.GREEN + "> ")
                        value = value.capitalize()
                        if value == "True" or value == "False":
                            data["flush_effect"] = value == "True"
                            os.system("cls")
                            print(Fore.GREEN + "Flush effect updated successfully!" + Style.RESET_ALL)
                            print("Returning to options menu...")
                            # Salvar o arquivo JSON com as alterações
                            with open("options.json", "w") as file:
                                json.dump(data, file, indent=4)  # indent=4 para facilitar a leitura do JSON
                            time.sleep(1.5)
                        else:
                            print(Fore.RED + "Invalid input! Please insert \"True\" or \"False\"." + Style.RESET_ALL)
                            time.sleep(2.55)
                    case 2:
                        while True:
                            try:
                                os.system("cls")
                                print(Fore.YELLOW + "Type show banner speed.\n" + Style.RESET_ALL)
                                print(Fore.GREEN + "The lower the value, the higher the speed.\nMax: 8\n" + Style.RESET_ALL)
                                print("Example: 6 = 0.006")
                                print("0: Deactivate banner flush effect\n")
                                value = float(input(Fore.GREEN+"> "+Style.RESET_ALL))
                                if value < 0:
                                    print(Fore.RED + "Invalid input! Please insert a positive value." + Style.RESET_ALL)
                                    time.sleep(3)
                                elif value > 8:
                                    print(Fore.RED + "Invalid input! Please insert a value less than or equal to 8." + Style.RESET_ALL)
                                    time.sleep(3)
                                else:
                                    data["show_banner_spd"] = value / 1000.0 if value != 0 else 0.0
                                    # Salvar o arquivo JSON com as alterações
                                    with open("options.json", "w") as file:
                                        json.dump(data, file, indent=4)  # indent=4 para facilitar a leitura do JSON
                                    print(Fore.GREEN + "Banner flush speed updated successfully!" + Style.RESET_ALL)
                                    time.sleep(2)
                                    break
                            except ValueError:
                                print(Fore.RED + "Invalid input! Please insert a valid number." + Style.RESET_ALL)
                                time.sleep(2.55)
                    case 3:
                        os.system("cls")
                        print(Fore.GREEN + "Type show words flush effect speed.\nThe lower the value, the higher the speed." + Style.RESET_ALL)
                        print(Fore.GREEN + "Max: 5\n" + Style.RESET_ALL)
                        print("Example: 5 = 0.05")
                        print("0: Deactivate words flush effect\n\n")
                        value = float(input(Fore.GREEN+"> "+Style.RESET_ALL))

                        if value < 0:
                            print(Fore.RED + "Invalid input! Please insert a positive value." + Style.RESET_ALL)
                            time.sleep(3)
                        elif value > 5:
                            print(Fore.RED + "Invalid input! Please insert a value less than or equal to 5." + Style.RESET_ALL)
                            time.sleep(3)
                        else:
                            data["show_words_spd"] = value / 100.0 if value != 0 else 0.0
                            # Salvar o arquivo JSON com as alterações
                            with open("options.json", "w") as file:
                                json.dump(data, file, indent=4)  # indent=4 para facilitar a leitura do JSON
                            print(Fore.GREEN + "Words flush speed updated successfully!" + Style.RESET_ALL)
                            time.sleep(3)
                    case 4:
                        print(Style.RESET_ALL + "Exiting...")
                        break
                    case _:
                        print(Fore.RED + "Invalid Option!" + Style.RESET_ALL)
                        time.sleep(3)
    except KeyboardInterrupt:
        print(Fore.RED + "Error." + Style.RESET_ALL)

