# tests/test_registration.py

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

from urls import REGISTER_URL, BASE_URL
from locators import StellarBurgersLocators
from helpers import generate_email, generate_password

def test_successful_registration():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(REGISTER_URL)
    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, StellarBurgersLocators.NAME_INPUT))
    )
    email_input = driver.find_element(By.XPATH, StellarBurgersLocators.EMAIL_INPUT)
    password_input = driver.find_element(By.XPATH, StellarBurgersLocators.PASSWORD_INPUT)
    register_button = driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_SUBMIT_BUTTON)

    name_input.send_keys("Test User")
    email_input.send_keys(generate_email())
    password_input.send_keys(generate_password())

    register_button.click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be(BASE_URL)
    )
    assert driver.current_url == BASE_URL
    driver.quit()

def test_invalid_password_error():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(REGISTER_URL)
    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, StellarBurgersLocators.NAME_INPUT))
    )
    email_input = driver.find_element(By.XPATH, StellarBurgersLocators.EMAIL_INPUT)
    password_input = driver.find_element(By.XPATH, StellarBurgersLocators.PASSWORD_INPUT)
    register_button = driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_SUBMIT_BUTTON)

    name_input.send_keys("Test User")
    email_input.send_keys(generate_email())
    password_input.send_keys("123")  # Меньше 6 символов

    register_button.click()

    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, StellarBurgersLocators.ERROR_MESSAGE))
    )
    assert "Некорректный пароль" in error_message.text
    driver.quit()

if __name__ == "__main__":
    test_successful_registration()
    print("✅ Успешная регистрация — OK")
    test_invalid_password_error()
    print("✅ Ошибка при коротком пароле — OK")
