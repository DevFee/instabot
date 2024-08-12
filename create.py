# libs
import requests
import time
import os
from colorama import Fore, Back, Style
import math
import json
from colorama import just_fix_windows_console

# config
just_fix_windows_console()

# Carregar o arquivo JSON
with open("bots.json", "r") as file:
    data = json.load(file)

# Control variables
max_bots = 100
min_bots = 10
import random

keyboard = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

first_names = [
    'John', 'Joseph', 'Robert', 'Louise', 'Peter', 'Carl', 'Carlo', 'Philipp', 'Estavan', 'Zoe', 'Lili', 'Anna', 'Lilia', 'Stephane',
    'Maria', 'David', 'Lucas', 'Ethan', 'Michael', 'Aiden', 'James', 'Benjamin', 'Isabella', 'Noah', 'Sophia', 'Emma', 'Ava', 'Olivia', 'Tahun'
]

last_names = [
    'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Rodriguez', 'Wilson', 'Anderson', 'Taylor', 'Thomas',
    'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Martinez', 'Robinson', 'Clark', 'Lewis', 'Lee', 'Walker',
]

def generate_random_nickname():
    nickname = ''
    for _ in range(12):
        nickname += random.choice(keyboard)
    return nickname

def generate_random_name():
    name = ''
    name += random.choice(first_names) + " " + random.choice(last_names)
    return name

def generate_random_email():
    email = ''
    for _ in range(14):
        email += random.choice(keyboard)
    response = requests.get("https://www.bing.com/ck/a?!&&p=fcf6374baffea76cJmltdHM9MTcyMzMzNDQwMCZpZ3VpZD0xMjMzZThkMC05MGRhLTY1NDUtM2RiZC1mYzA3OTE4ZDY0NTcmaW5zaWQ9NTE5MA&ptn=3&ver=2&hsh=3&fclid=1233e8d0-90da-6545-3dbd-fc07918d6457&u=a1aHR0cHM6Ly9wcm90b24ubWUvcHQtYnIvbWFpbA&ntb=1")
    return email

def generate_random_password():
    password = ''
    for _ in range(8):
        password += random.choice(keyboard)
    return password

def create_bots(quantity):
    if quantity > max_bots or quantity < min_bots:
        print(f"The quantity must be less than {max_bots} and must be greater than {min_bots}.")
    else:
        print("Establishing connection")
        response = requests.get("https://instagram.com")
        if response.status_code == 200:
            print(Fore.GREEN + "Connected successfully!\n" + Style.RESET_ALL)
            time.sleep(0.5)
            os.system("cls")
            print(Fore.WHITE + f"Creating {quantity} bots...")
            for i in range(quantity):
                nickname = generate_random_nickname()
                password = generate_random_password()
                email = generate_random_email()
                name = generate_random_name()
                
                user = {
                    "name": name,
                    "username": nickname,
                    "password": password,
                    "email": email
                }

                # Adiciona o novo bot à lista existente em 'data'
                data.append(user)

                # Salva as mudanças no arquivo JSON
                with open("bots.json", 'w') as file:
                    json.dump(data, file, indent=4)  # indent=4 para facilitar a leitura do JSON
                
                print(user)
            print(Fore.GREEN + f"Successfully created {quantity} bots!" + Style.RESET_ALL)