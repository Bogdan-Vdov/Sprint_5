# tests/test_login.py

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

from urls import BASE_URL, LOGIN_URL
from locators import StellarBurgersLocators

def test_login_main_page_button():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(BASE_URL)
    login_button = driver.find_element(By.XPATH, StellarBurgersLocators.LOGIN_BUTTON_MAIN)
    login_button.click()
    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )
    assert "/login" in driver.current_url
    driver.quit()

def test_login_account_link():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(BASE_URL)
    account_link = driver.find_element(By.XPATH, StellarBurgersLocators.ACCOUNT_LINK)
    account_link.click()
    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )
    assert "/login" in driver.current_url
    driver.quit()

def test_login_registration_form_link():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(f"{BASE_URL}/register")
    login_link = driver.find_element(By.XPATH, "//a[text()='Войти']")
    login_link.click()
    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )
    assert "/login" in driver.current_url
    driver.quit()

def test_login_forgot_password_link():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(f"{BASE_URL}/forgot-password")
    login_link = driver.find_element(By.XPATH, "//a[text()='Войти']")
    login_link.click()
    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )
    assert "/login" in driver.current_url
    driver.quit()

if __name__ == "__main__":
    test_login_main_page_button()
    print("✅ Вход через кнопку на главной — OK")
    test_login_account_link()
    print("✅ Вход через личный кабинет — OK")
    test_login_registration_form_link()
    print("✅ Вход через ссылку в регистрации — OK")
    test_login_forgot_password_link()
    print("✅ Вход через ссылку в восстановлении — OK")