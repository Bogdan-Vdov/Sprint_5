# helpers.py

import random
import string

def generate_email():
    """Генерирует уникальный email в формате имя_фамилия_номер@yandex.ru"""
    name = "testuser"
    number = random.randint(1000, 9999)
    return f"{name}{number}@yandex.ru"

def generate_password():
    """Генерирует пароль из 6 символов (буквы + цифры)"""
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))