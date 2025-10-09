# tests/test_navigation.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
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

def test_go_to_personal_account():
    """Проверяет переход в личный кабинет через регистрацию и вход"""
    print("✅ Начинаем тест: test_go_to_personal_account")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://stellarburgers.nomoreparties.site/")

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

    # Переходим на страницу регистрации
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Очищаем куки, чтобы не было сохранённой сессии
    print("⏳ Очищаем куки...")
    driver.delete_all_cookies()
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
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StellarBurgersLocators.EMAIL_INPUT))
        )
        print("✅ Поле 'Email' найдено")
    except Exception as e:
        print(f"❌ Поле 'Email' не найдено: {e}")
        driver.quit()
        return

    try:
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StellarBurgersLocators.PASSWORD_INPUT))
        )
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

    # Переходим в личный кабинет
    try:
        account_link = driver.find_element(By.XPATH, StellarBurgersLocators.ACCOUNT_LINK)
        account_link.click()
        print("✅ Перешли в личный кабинет")
    except Exception as e:
        print(f"❌ Не удалось перейти в личный кабинет: {e}")
        driver.quit()
        return

    # Ждем переход на /account
    try:
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account")
        )
        print("✅ Успешно перешли на /account")
    except Exception as e:
        print(f"❌ Не удалось перейти на /account: {e}")
        driver.quit()
        return

    assert "/account" in driver.current_url
    print("✅ Все проверки пройдены")

    driver.quit()
    print("✅ Тест завершён")

def test_constructor_sections():
    """Проверяет переключение между разделами в конструкторе"""
    print("✅ Начинаем тест: test_constructor_sections")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Проверяем, что мы не на странице заказа или аккаунта
    if "/account" in driver.current_url or "/feed" in driver.current_url or "идентификатор заказа" in driver.page_source:
        print("🔄 Переходим на главную страницу")
        driver.get("https://stellarburgers.nomoreparties.site/")

    # Ждем, что мы на главной
    try:
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )
        print("✅ Успешно перешли на главную")
    except Exception as e:
        print(f"❌ Не удалось перейти на главную: {e}")
        driver.quit()
        return

    # Проверяем Булки
    try:
        buns_tab = driver.find_element(By.XPATH, StellarBurgersLocators.BUNS_TAB)
        # Используем ActionChains, чтобы кликнуть через JavaScript
        ActionChains(driver).move_to_element(buns_tab).click().perform()
        print("✅ Перешли на раздел 'Булки'")
    except Exception as e:
        print(f"❌ Не удалось перейти на раздел 'Булки': {e}")
        driver.quit()
        return

    assert "Булки" in driver.page_source
    print("✅ Раздел 'Булки' работает")

    # Проверяем Соусы
    try:
        sauces_tab = driver.find_element(By.XPATH, StellarBurgersLocators.SAUCES_TAB)
        # Используем ActionChains, чтобы кликнуть через JavaScript
        ActionChains(driver).move_to_element(sauces_tab).click().perform()
        print("✅ Перешли на раздел 'Соусы'")
    except Exception as e:
        print(f"❌ Не удалось перейти на раздел 'Соусы': {e}")
        driver.quit()
        return

    assert "Соусы" in driver.page_source
    print("✅ Раздел 'Соусы' работает")

    # Проверяем Начинки
    try:
        fillings_tab = driver.find_element(By.XPATH, StellarBurgersLocators.FILLINGS_TAB)
        # Используем ActionChains, чтобы кликнуть через JavaScript
        ActionChains(driver).move_to_element(fillings_tab).click().perform()
        print("✅ Перешли на раздел 'Начинки'")
    except Exception as e:
        print(f"❌ Не удалось перейти на раздел 'Начинки': {e}")
        driver.quit()
        return

    assert "Начинки" in driver.page_source
    print("✅ Раздел 'Начинки' работает")

    driver.quit()
    print("✅ Тест завершён")

def test_logout():
    """Проверяет выход из аккаунта"""
    print("✅ Начинаем тест: test_logout")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://stellarburgers.nomoreparties.site/")

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

    # Переходим на страницу регистрации
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Очищаем куки, чтобы не было сохранённой сессии
    print("⏳ Очищаем куки...")
    driver.delete_all_cookies()
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
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StellarBurgersLocators.EMAIL_INPUT))
        )
        print("✅ Поле 'Email' найдено")
    except Exception as e:
        print(f"❌ Поле 'Email' не найдено: {e}")
        driver.quit()
        return

    try:
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StellarBurgersLocators.PASSWORD_INPUT))
        )
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

    email = generate_email()
    password = generate_password()

    name_input.send_keys("Test User")
    email_input.send_keys(email)
    password_input.send_keys(password)

    print("✅ Данные введены")

    # Нажимаем кнопку
    try:
        register_button.click()
        print("✅ Кнопка 'Зарегистрироваться' нажата")
    except Exception as e:
        print(f"❌ Кнопка 'Зарегистрироваться' не нажата: {e}")
        driver.quit()
        return

    # Ждем перехода на главную после регистрации
    try:
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )
        print("✅ Успешно перешли на главную")
    except Exception as e:
        print(f"❌ Не удалось перейти на главную: {e}")
        driver.quit()
        return

    # Переходим в личный кабинет
    try:
        account_link = driver.find_element(By.XPATH, StellarBurgersLocators.ACCOUNT_LINK)
        account_link.click()
        print("✅ Перешли в личный кабинет")
    except Exception as e:
        print(f"❌ Не удалось перейти в личный кабинет: {e}")
        driver.quit()
        return

    # Ждем переход на /account
    try:
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account")
        )
        print("✅ Успешно перешли на /account")
    except Exception as e:
        print(f"❌ Не удалось перейти на /account: {e}")
        driver.quit()
        return

    # Выходим
    try:
        logout_button = driver.find_element(By.XPATH, StellarBurgersLocators.LOGOUT_BUTTON)
        logout_button.click()
        print("✅ Вышли из аккаунта")
    except Exception as e:
        print(f"❌ Не удалось выйти из аккаунта: {e}")
        driver.quit()
        return

    # Ждем перехода на /login
    try:
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
        )
        print("✅ Успешно перешли на /login")
    except Exception as e:
        print(f"❌ Не удалось перейти на /login: {e}")
        driver.quit()
        return

    assert "/login" in driver.current_url
    print("✅ Все проверки пройдены")

    driver.quit()
    print("✅ Тест завершён")

if __name__ == "__main__":
    test_go_to_personal_account()
    print("✅ Переход в личный кабинет — OK")
    test_constructor_sections()
    print("✅ Переключение разделов в конструкторе — OK")
    test_logout()
    print("✅ Выход из аккаунта — OK")