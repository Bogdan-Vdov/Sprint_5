# tests/test_navigation.py

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Исправленный импорт
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from urls import ACCOUNT_URL, BASE_URL, LOGIN_URL, REGISTER_URL
from locators import StellarBurgersLocators
from helpers import generate_email, generate_password

class TestNavigation:
    """
    Тесты для проверки навигации по сайту.
    """

    def test_go_to_personal_account(self, driver):
        """
        Проверяет переход в личный кабинет через регистрацию и вход.
        """
        # Arrange & Act: Открытие страницы регистрации
        driver.get(REGISTER_URL)
        # Очистка куки для гарантии "чистого" состояния
        driver.delete_all_cookies()
        # Повторный переход для уверенности, что куки очищены
        driver.get(REGISTER_URL)

        # Явное ожидание загрузки формы регистрации
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, StellarBurgersLocators.REGISTRATION_FORM))
        )

        # Assert: Проверка наличия формы и полей
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StellarBurgersLocators.NAME_INPUT))
        )
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StellarBurgersLocators.EMAIL_INPUT))
        )
        password_input = driver.find_element(By.XPATH, StellarBurgersLocators.PASSWORD_INPUT)
        register_submit_button = driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_SUBMIT_BUTTON)

        # Генерация тестовых данных
        email = generate_email()
        password = generate_password()

        # Заполнение формы
        name_input.send_keys("Test User")
        email_input.send_keys(email)
        password_input.send_keys(password)

        # Отправка формы
        register_submit_button.click()

        # Ожидание перехода на страницу логина (если требуется)
        WebDriverWait(driver, 10).until(
                EC.url_to_be(LOGIN_URL)
        )
        # Ввод учетных данных для входа
        login_email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StellarBurgersLocators.LOGIN_EMAIL_INPUT))
        )
        login_password_input = driver.find_element(By.XPATH, StellarBurgersLocators.LOGIN_PASSWORD_INPUT)
        login_button = driver.find_element(By.XPATH, StellarBurgersLocators.LOGIN_SUBMIT_BUTTON)

        login_email_input.send_keys(email)
        login_password_input.send_keys(password)
        login_button.click()

        # Переход в личный кабинет снова
        account_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, StellarBurgersLocators.ACCOUNT_LINK))
        )
        account_link.click()

        # Ожидание URL личного кабинета
        WebDriverWait(driver, 10).until(
            EC.url_contains(ACCOUNT_URL)
        )
        assert ACCOUNT_URL in driver.current_url

    # --- Тесты для конструктора ---
    # Каждый тест проверяет один конкретный сценарий
    def test_constructor_buns(self, driver):
        """
        Проверяет активность раздела 'Булки' в конструкторе.
        """
        # Arrange
        driver.get(BASE_URL)

        # Act & Assert: Проверяем Булки
        buns_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, StellarBurgersLocators.BUNS_TAB))
        )
        ActionChains(driver).move_to_element(buns_tab).click().perform()
        # Проверка: элемент активен (атрибут class содержит 'tab_tab_type_current')
        assert "tab_tab_type_current" in buns_tab.get_attribute("class"), "Раздел 'Булки' не активен"

    def test_constructor_sauces(self, driver):
        """
        Проверяет активность раздела 'Соусы' в конструкторе.
        """
        # Arrange
        driver.get(BASE_URL)

        # Act & Assert: Проверяем Соусы
        sauces_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, StellarBurgersLocators.SAUCES_TAB))
        )
        ActionChains(driver).move_to_element(sauces_tab).click().perform()
        assert "tab_tab_type_current" in sauces_tab.get_attribute("class"), "Раздел 'Соусы' не активен"

    def test_constructor_fillings(self, driver):
        """
        Проверяет активность раздела 'Начинки' в конструкторе.
        """
        # Arrange
        driver.get(BASE_URL)

        # Act & Assert: Проверяем Начинки
        fillings_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, StellarBurgersLocators.FILLINGS_TAB))
        )
        ActionChains(driver).move_to_element(fillings_tab).click().perform()
        assert "tab_tab_type_current" in fillings_tab.get_attribute("class"), "Раздел 'Начинки' не активен"

    def test_logout(self, driver):
        """
        Проверяет выход из аккаунта.
        """
        # Arrange: Регистрация нового пользователя
        driver.get(REGISTER_URL)
        driver.delete_all_cookies()
        driver.get(REGISTER_URL)

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, StellarBurgersLocators.REGISTRATION_FORM))
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

        # Ожидание перехода на страницу логина (если требуется)
        WebDriverWait(driver, 10).until(
            EC.url_to_be(LOGIN_URL)
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

        # Переходим в личный кабинет
        account_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, StellarBurgersLocators.ACCOUNT_LINK))
        )
        account_link.click()

        # Выходим
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, StellarBurgersLocators.LOGOUT_BUTTON))
        )
        logout_button.click()

        # Assert: Проверка перехода на страницу логина после выхода
        WebDriverWait(driver, 10).until(
            EC.url_to_be(LOGIN_URL) # TODO: Исправить на Urls.py
        )
        assert LOGIN_URL in driver.current_url
