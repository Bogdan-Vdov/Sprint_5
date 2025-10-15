# tests/test_registration.py

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Исправленный импорт
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from urls import BASE_URL, REGISTER_URL, LOGIN_URL
from locators import StellarBurgersLocators
from helpers import generate_email, generate_password

class TestRegistration:
    """
    Тесты для проверки функциональности регистрации.
    """

    def test_successful_registration(self, driver):
        """
        Проверяет успешную регистрацию нового пользователя.
        """
        # Arrange: Открытие страницы регистрации
        driver.get(REGISTER_URL)
        # Очистка куки
        driver.delete_all_cookies()
        # Повторный переход
        driver.get(REGISTER_URL)

        # Явное ожидание загрузки формы регистрации
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, StellarBurgersLocators.REGISTRATION_FORM))
        )

        # Assert & Act: Проверка наличия полей и заполнение
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StellarBurgersLocators.NAME_INPUT))
        )
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StellarBurgersLocators.EMAIL_INPUT))
        )
        password_input = driver.find_element(By.XPATH, StellarBurgersLocators.PASSWORD_INPUT)
        register_submit_button = driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_SUBMIT_BUTTON)

        # Заполнение формы
        name_input.send_keys("Test User")
        email = generate_email()
        email_input.send_keys(email)
        password = generate_password()
        password_input.send_keys(password)

        # Отправка формы
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
        assert logout_button.is_displayed(), "Отсутствует кнопка 'Выход'"

    def test_invalid_password_error(self, driver):
        """
        Проверяет появление ошибки при вводе некорректного пароля (меньше 6 символов).
        """
        # Arrange: Открытие страницы регистрации
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

        # Act: Заполнение формы с коротким паролем
        name_input.send_keys("Test User")
        email_input.send_keys(generate_email())
        # Вводим пароль меньше 6 символов
        password_input.send_keys("123")

        # Отправка формы
        register_submit_button.click()

        # Assert: Ожидание и проверка сообщения об ошибке
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, StellarBurgersLocators.ERROR_MESSAGE))
        )
        # Проверяем, что сообщение об ошибке отображается
        assert error_message.is_displayed(), "Сообщение об ошибке не отображается"