import random
import requests

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

url = "https://account.proton.me/mail/signup?plan=free&ref=mail_plus_intro-mailpricing-2&currency=EUR"  # Este URL é apenas um exemplo. Você deve confirmar o endpoint correto.

def generate_username():
    return ''.join(random.choice(keyboard) for _ in range(14))

def generate_random_name():
    return random.choice(first_names) + " " + random.choice(last_names)

def generate_random_password():
    return ''.join(random.choice(keyboard) for _ in range(8))

password = generate_random_password()
full_name = generate_random_name()
username = generate_username()

data = {
    'username': username,
    'name': full_name,
    'password': password,
    'confirm_password': password
}

# Cabeçalhos necessários (exemplo)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',  # ou 'application/json', dependendo do que a API espera
    # Outros cabeçalhos, como tokens CSRF ou cookies, podem ser necessários
}

# Enviando a solicitação POST
response = requests.post(url, data=data, headers=headers)

# Verificando a resposta
print(response.status_code)
print(response.text)
