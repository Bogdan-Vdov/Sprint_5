# tests/test_navigation.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Исправленный импорт
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from urls import BASE_URL, ACCOUNT_URL
from locators import StellarBurgersLocators
from helpers import generate_email, generate_password

class TestNavigation:
    def test_go_to_personal_account(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(f"{BASE_URL}/register")

        # Очищаем куки, чтобы не было сохранённой сессии
        driver.delete_all_cookies()
        driver.get(f"{BASE_URL}/register")

        # Ждем появления формы регистрации
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//form"))
        )

        # Ждем появления поля "Имя"
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StellarBurgersLocators.NAME_INPUT))
        )
        # Теперь ищем остальные поля
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StellarBurgersLocators.EMAIL_INPUT))
        )
        password_input = driver.find_element(By.XPATH, StellarBurgersLocators.PASSWORD_INPUT)
        register_submit_button = driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_SUBMIT_BUTTON)

        email = generate_email()
        password = generate_password()

        name_input.send_keys("Test User")
        email_input.send_keys(email)
        password_input.send_keys(password)

        register_submit_button.click()

        # Ждем перехода на главную после регистрации
        WebDriverWait(driver, 10).until(
            EC.url_to_be(BASE_URL)
        )

        # Переходим в личный кабинет
        account_link = driver.find_element(By.XPATH, StellarBurgersLocators.ACCOUNT_LINK)
        account_link.click()

        # Ждем перехода на /login
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

    def test_constructor_sections(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(BASE_URL)

        # Проверяем Булки
        buns_tab = driver.find_element(By.XPATH, StellarBurgersLocators.BUNS_TAB)
        ActionChains(driver).move_to_element(buns_tab).click().perform()
        assert "Булки" in driver.page_source

        # Проверяем Соусы
        sauces_tab = driver.find_element(By.XPATH, StellarBurgersLocators.SAUCES_TAB)
        ActionChains(driver).move_to_element(sauces_tab).click().perform()
        assert "Соусы" in driver.page_source

        # Проверяем Начинки
        fillings_tab = driver.find_element(By.XPATH, StellarBurgersLocators.FILLINGS_TAB)
        ActionChains(driver).move_to_element(fillings_tab).click().perform()
        assert "Начинки" in driver.page_source

        driver.quit()

    def test_logout(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(f"{BASE_URL}/register")

        # Очищаем куки, чтобы не было сохранённой сессии
        driver.delete_all_cookies()
        driver.get(f"{BASE_URL}/register")

        # Ждем появления формы регистрации
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//form"))
        )

        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StellarBurgersLocators.NAME_INPUT))
        )
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StellarBurgersLocators.EMAIL_INPUT))
        )
        password_input = driver.find_element(By.XPATH, StellarBurgersLocators.PASSWORD_INPUT)
        register_submit_button = driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_SUBMIT_BUTTON)

        email = generate_email()
        password = generate_password()

        name_input.send_keys("Test User")
        email_input.send_keys(email)
        password_input.send_keys(password)

        register_submit_button.click()

        # Ждем перехода на главную после регистрации
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