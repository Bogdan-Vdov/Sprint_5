# tests/test_navigation.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Исправленный импорт
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from urls import BASE_URL, ACCOUNT_URL
from locators import StellarBurgersLocators
from helpers import generate_email, generate_password

def test_go_to_personal_account():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # Регистрация нового пользователя
    driver.get(f"{BASE_URL}/register")
    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, StellarBurgersLocators.NAME_INPUT))
    )
    email_input = driver.find_element(By.XPATH, StellarBurgersLocators.EMAIL_INPUT)
    password_input = driver.find_element(By.XPATH, StellarBurgersLocators.PASSWORD_INPUT)
    register_submit_button = driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_SUBMIT_BUTTON)

    email = generate_email()
    password = generate_password()

    name_input.send_keys("Test User")
    email_input.send_keys(email)
    password_input.send_keys(password)

    register_submit_button.click()

    # Ждем переход на главную после регистрации
    WebDriverWait(driver, 10).until(
        EC.url_to_be(BASE_URL)
    )

    # Переходим в личный кабинет
    account_link = driver.find_element(By.XPATH, StellarBurgersLocators.ACCOUNT_LINK)
    account_link.click()

    # Ждем переход на /login
    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )

    # Вводим логин и пароль
    login_email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, StellarBurgersLocators.LOGIN_EMAIL_INPUT))
    )
    login_password_input = driver.find_element(By.XPATH, StellarBurgersLocators.LOGIN_PASSWORD_INPUT)
    login_button = driver.find_element(By.XPATH, StellarBurgersLocators.LOGIN_SUBMIT_BUTTON)

    login_email_input.send_keys(email)
    login_password_input.send_keys(password)
    login_button.click()

    # После входа ожидаем переход на главную
    WebDriverWait(driver, 10).until(
        EC.url_to_be(BASE_URL)
    )

    # Шаг 3: Теперь переходим в личный кабинет
    account_link = driver.find_element(By.XPATH, StellarBurgersLocators.ACCOUNT_LINK)
    account_link.click()

    # И ожидаем URL /account
    WebDriverWait(driver, 10).until(
        EC.url_contains("/account")
    )
    assert "/account" in driver.current_url

    driver.quit()

def test_constructor_sections():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(BASE_URL)

    # Проверяем Булки
    buns_tab = driver.find_element(By.XPATH, StellarBurgersLocators.BUNS_TAB)
    buns_tab.click()
    assert "Булки" in driver.page_source

    # Проверяем Соусы
    sauces_tab = driver.find_element(By.XPATH, StellarBurgersLocators.SAUCES_TAB)
    sauces_tab.click()
    assert "Соусы" in driver.page_source

    # Проверяем Начинки
    fillings_tab = driver.find_element(By.XPATH, StellarBurgersLocators.FILLINGS_TAB)
    fillings_tab.click()
    assert "Начинки" in driver.page_source

    driver.quit()

def test_logout():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # Регистрация нового пользователя
    driver.get(f"{BASE_URL}/register")
    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, StellarBurgersLocators.NAME_INPUT))
    )
    email_input = driver.find_element(By.XPATH, StellarBurgersLocators.EMAIL_INPUT)
    password_input = driver.find_element(By.XPATH, StellarBurgersLocators.PASSWORD_INPUT)
    register_submit_button = driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_SUBMIT_BUTTON)

    email = generate_email()
    password = generate_password()

    name_input.send_keys("Test User")
    email_input.send_keys(email)
    password_input.send_keys(password)

    register_submit_button.click()

    # Ждем переход на главную после регистрации
    WebDriverWait(driver, 10).until(
        EC.url_to_be(BASE_URL)
    )

    # Переходим в личный кабинет
    account_link = driver.find_element(By.XPATH, StellarBurgersLocators.ACCOUNT_LINK)
    account_link.click()

    # Вводим логин и пароль
    login_email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, StellarBurgersLocators.LOGIN_EMAIL_INPUT))
    )
    login_password_input = driver.find_element(By.XPATH, StellarBurgersLocators.LOGIN_PASSWORD_INPUT)
    login_button = driver.find_element(By.XPATH, StellarBurgersLocators.LOGIN_SUBMIT_BUTTON)

    login_email_input.send_keys(email)
    login_password_input.send_keys(password)
    login_button.click()

    # После входа ожидаем переход на главную
    WebDriverWait(driver, 10).until(
        EC.url_to_be(BASE_URL)
    )

    # Переходим в личный кабинет
    account_link = driver.find_element(By.XPATH, StellarBurgersLocators.ACCOUNT_LINK)
    account_link.click()

    # Выходим
    logout_button = driver.find_element(By.XPATH, StellarBurgersLocators.LOGOUT_BUTTON)
    logout_button.click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be(f"{BASE_URL}/login")
    )
    assert "/login" in driver.current_url

    driver.quit()

if __name__ == "__main__":
    test_go_to_personal_account()
    print("✅ Переход в личный кабинет — OK")
    test_constructor_sections()
    print("✅ Переключение разделов в конструкторе — OK")
    test_logout()
    print("✅ Выход из аккаунта — OK")