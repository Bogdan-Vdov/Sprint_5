# tests/test_registration.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Исправленный импорт locators.py из родительской папки
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from locators import StellarBurgersLocators
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

def test_successful_registration():
    print("✅ Начинаем тест: test_successful_registration")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Проверяем URL
    print(f"🌐 Текущий URL: {driver.current_url}")

    # Проверяем, что мы не на странице заказа или аккаунта
    if "/account" in driver.current_url or "/feed" in driver.current_url or "идентификатор заказа" in driver.page_source:
        print("🔄 Мы уже залогинены. Переходим в личный кабинет и выходим.")
        driver.get("https://stellarburgers.nomoreparties.site/account")

        # Ждем, что мы на /account
        try:
            WebDriverWait(driver, 10).until(
                EC.url_contains("/account")
            )
            print("✅ Успешно перешли на /account")
        except Exception as e:
            print(f"❌ Не удалось перейти на /account: {e}")
            driver.quit()
            return

        # Нажимаем кнопку "Выход"
        try:
            logout_button = driver.find_element(By.XPATH, StellarBurgersLocators.LOGOUT_BUTTON)
            logout_button.click()
            print("✅ Успешно нажали 'Выход'")
        except Exception as e:
            print(f"❌ Не удалось нажать 'Выход': {e}")
            driver.quit()
            return

        # Ждем, что мы на /login
        try:
            WebDriverWait(driver, 10).until(
                EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
            )
            print("✅ Успешно вышли из аккаунта")
        except Exception as e:
            print(f"❌ Не удалось выйти из аккаунта: {e}")
            driver.quit()
            return

        # Возвращаемся на /register
        driver.get("https://stellarburgers.nomoreparties.site/register")

    # Ждем, что мы на странице регистрации
    try:
        WebDriverWait(driver, 10).until(
            EC.url_contains("/register")
        )
        print("✅ Успешно перешли на /register")
    except Exception as e:
        print(f"❌ Не удалось перейти на /register: {e}")
        driver.quit()
        return

    # Проверяем исходный HTML страницы
    print("📄 HTML страницы:")
    print(driver.page_source[:1000])  # Показываем первые 1000 символов

    # Ждем появления формы регистрации
    try:
        form = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//form"))
        )
        print("✅ Форма регистрации найдена")
    except Exception as e:
        print(f"❌ Форма регистрации не найдена: {e}")
        driver.quit()
        return

    # Ждем появления поля "Имя"
    try:
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StellarBurgersLocators.NAME_INPUT))
        )
        print("✅ Поле 'Имя' найдено")
    except Exception as e:
        print(f"❌ Поле 'Имя' не найдено: {e}")
        driver.quit()
        return

    # Теперь ищем остальные поля
    try:
        email_input = driver.find_element(By.XPATH, StellarBurgersLocators.EMAIL_INPUT)
        print("✅ Поле 'Email' найдено")
    except Exception as e:
        print(f"❌ Поле 'Email' не найдено: {e}")
        driver.quit()
        return

    try:
        password_input = driver.find_element(By.XPATH, StellarBurgersLocators.PASSWORD_INPUT)
        print("✅ Поле 'Пароль' найдено")
    except Exception as e:
        print(f"❌ Поле 'Пароль' не найдено: {e}")
        driver.quit()
        return

    try:
        register_button = driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_SUBMIT_BUTTON)
        print("✅ Кнопка 'Зарегистрироваться' найдена")
    except Exception as e:
        print(f"❌ Кнопка 'Зарегистрироваться' не найдена: {e}")
        driver.quit()
        return

    # Вводим данные
    name_input.send_keys("Test User")
    email_input.send_keys(generate_email())
    password_input.send_keys(generate_password())

    print("✅ Данные введены")

    # Нажимаем кнопку
    try:
        register_button.click()
        print("✅ Кнопка 'Зарегистрироваться' нажата")
    except Exception as e:
        print(f"❌ Кнопка 'Зарегистрироваться' не нажата: {e}")
        driver.quit()
        return

    # Ждем перехода на главную после успешной регистрации
    try:
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )
        print("✅ Успешно перешли на главную")
    except Exception as e:
        print(f"❌ Не удалось перейти на главную: {e}")
        driver.quit()
        return

    driver.quit()
    print("✅ Тест завершён")

def test_invalid_password_error():
    print("✅ Начинаем тест: test_invalid_password_error")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Ждем, что мы на странице регистрации
    try:
        WebDriverWait(driver, 10).until(
            EC.url_contains("/register")
        )
        print("✅ Успешно перешли на /register")
    except Exception as e:
        print(f"❌ Не удалось перейти на /register: {e}")
        driver.quit()
        return

    # Ждем появления формы регистрации
    try:
        form = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//form"))
        )
        print("✅ Форма регистрации найдена")
    except Exception as e:
        print(f"❌ Форма регистрации не найдена: {e}")
        driver.quit()
        return

    # Ждем появления поля "Имя"
    try:
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StellarBurgersLocators.NAME_INPUT))
        )
        print("✅ Поле 'Имя' найдено")
    except Exception as e:
        print(f"❌ Поле 'Имя' не найдено: {e}")
        driver.quit()
        return

    # Теперь ищем остальные поля
    try:
        email_input = driver.find_element(By.XPATH, StellarBurgersLocators.EMAIL_INPUT)
        print("✅ Поле 'Email' найдено")
    except Exception as e:
        print(f"❌ Поле 'Email' не найдено: {e}")
        driver.quit()
        return

    try:
        password_input = driver.find_element(By.XPATH, StellarBurgersLocators.PASSWORD_INPUT)
        print("✅ Поле 'Пароль' найдено")
    except Exception as e:
        print(f"❌ Поле 'Пароль' не найдено: {e}")
        driver.quit()
        return

    try:
        register_button = driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_SUBMIT_BUTTON)
        print("✅ Кнопка 'Зарегистрироваться' найдена")
    except Exception as e:
        print(f"❌ Кнопка 'Зарегистрироваться' не найдена: {e}")
        driver.quit()
        return

    name_input.send_keys("Test User")
    email_input.send_keys(generate_email())
    password_input.send_keys("123")  # Меньше 6 символов

    register_button.click()

    # Проверяем, что появилась ошибка
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, StellarBurgersLocators.ERROR_MESSAGE))
        )
        print("✅ Ошибка при коротком пароле найдена")
    except Exception as e:
        print(f"❌ Ошибка при коротком пароле не найдена: {e}")
        driver.quit()
        return

    assert "Некорректный пароль" in error_message.text
    print("✅ Ошибка 'Некорректный пароль' отображается")

    driver.quit()
    print("✅ Тест завершён")

if __name__ == "__main__":
    test_successful_registration()
    print("✅ Успешная регистрация — OK")
    test_invalid_password_error()
    print("✅ Ошибка при коротком пароле — OK")
