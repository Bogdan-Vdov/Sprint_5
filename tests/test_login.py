# tests/test_login.py

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from urls import BASE_URL, FORGOT_PASSWORD_URL, LOGIN_URL, REGISTER_URL
from locators import StellarBurgersLocators


class TestLogin:

    def test_login_main_page_button(self, driver):
        driver.get(BASE_URL)
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, StellarBurgersLocators.LOGIN_BUTTON_MAIN))
        )
        login_button.click()
        WebDriverWait(driver, 10).until(
            EC.url_contains(LOGIN_URL)
        )
        assert LOGIN_URL in driver.current_url

    def test_login_account_link(self, driver):
        driver.get(BASE_URL)
        account_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, StellarBurgersLocators.ACCOUNT_LINK))
        )
        account_link.click()
        WebDriverWait(driver, 10).until(
            EC.url_contains(LOGIN_URL)
        )
        assert LOGIN_URL in driver.current_url

    def test_login_registration_form_link(self, driver):
        driver.get(REGISTER_URL)
        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, StellarBurgersLocators.LOGIN_LINK_IN_REGISTRATION_FORM))
        )
        login_link.click()
        WebDriverWait(driver, 10).until(
            EC.url_contains(LOGIN_URL)
        )
        assert LOGIN_URL in driver.current_url

    def test_login_forgot_password_link(self, driver):
        driver.get(FORGOT_PASSWORD_URL)
        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, StellarBurgersLocators.LOGIN_LINK_IN_FORGOT_PASSWORD_FORM))
        )
        login_link.click()
        WebDriverWait(driver, 10).until(
            EC.url_contains(LOGIN_URL)
        )
        assert LOGIN_URL in driver.current_url
