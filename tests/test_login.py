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

from urls import BASE_URL
from locators import StellarBurgersLocators

class TestLogin:
    def test_login_main_page_button(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(BASE_URL)
        login_button = driver.find_element(By.XPATH, StellarBurgersLocators.LOGIN_BUTTON_MAIN)
        login_button.click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        assert "/login" in driver.current_url
        driver.quit()

    def test_login_account_link(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(BASE_URL)
        account_link = driver.find_element(By.XPATH, StellarBurgersLocators.ACCOUNT_LINK)
        account_link.click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        assert "/login" in driver.current_url
        driver.quit()

    def test_login_registration_form_link(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(f"{BASE_URL}/register")
        login_link = driver.find_element(By.XPATH, StellarBurgersLocators.LOGIN_LINK_IN_REGISTRATION_FORM)
        login_link.click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        assert "/login" in driver.current_url
        driver.quit()

    def test_login_forgot_password_link(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(f"{BASE_URL}/forgot-password")
        login_link = driver.find_element(By.XPATH, StellarBurgersLocators.LOGIN_LINK_IN_FORGOT_PASSWORD_FORM)
        login_link.click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        assert "/login" in driver.current_url
        driver.quit()