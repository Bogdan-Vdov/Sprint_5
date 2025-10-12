# tests/test_login.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Исправленный импорт
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from urls import BASE_URL
from locators import StellarBurgersLocators

class TestLogin:

    def test_login_main_page_button(self, driver):
     
        # Открытие главной страницы
        driver.get(BASE_URL)

        # Поиск и клик по кнопке входа
        login_button = driver.find_element(By.XPATH, StellarBurgersLocators.LOGIN_BUTTON_MAIN)
        login_button.click()

        # Ожидание перехода на страницу логина
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        # Проверка URL
        assert "/login" in driver.current_url


    def test_login_account_link(self, driver):
    
        # Arrange
        driver.get(BASE_URL)

        # Act
        account_link = driver.find_element(By.XPATH, StellarBurgersLocators.ACCOUNT_LINK)
        account_link.click()

        # Assert
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        assert "/login" in driver.current_url
      

    def test_login_registration_form_link(self, driver):

        # Arrange
        registration_url = f"{BASE_URL}/register"
        driver.get(registration_url)

        # Act
        login_link = driver.find_element(By.XPATH, "//a[text()='Войти']")
        login_link.click()

        # Assert
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        assert "/login" in driver.current_url
    

    def test_login_forgot_password_link(self, driver):
   
        # Arrange
        forgot_password_url = f"{BASE_URL}/forgot-password"
        driver.get(forgot_password_url)

        # Act
        login_link = driver.find_element(By.XPATH, "//a[text()='Войти']")
        login_link.click()

        # Assert
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        assert "/login" in driver.current_url