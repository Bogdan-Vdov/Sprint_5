# locators.py

class StellarBurgersLocators:
    # Главная страница
    REGISTER_BUTTON = "//button[text()='Зарегистрироваться']"
    LOGIN_BUTTON_MAIN = "//button[text()='Войти в аккаунт']"
    CONSTRUCTOR_LINK = "//a[@href='/']"
    ACCOUNT_LINK = "//a[@href='/account']"

    # Страница регистрации
    REGISTRATION_FORM = "//form" # Новый локатор
    NAME_INPUT = "//input[@name='name']"
    EMAIL_INPUT = "//input[@name='email']"
    PASSWORD_INPUT = "//input[@name='password']"
    REGISTER_SUBMIT_BUTTON = "//button[text()='Зарегистрироваться']"
    ERROR_MESSAGE = "//p[contains(@class, 'input__error')]"
    LOGIN_LINK_IN_REGISTRATION_FORM = "//a[text()='Войти']" # Новый локатор

    # Страница входа
    LOGIN_EMAIL_INPUT = "//input[@name='email']"
    LOGIN_PASSWORD_INPUT = "//input[@name='password']"
    LOGIN_SUBMIT_BUTTON = "//button[text()='Войти']"
    FORGOT_PASSWORD_LINK = "//a[text()='Восстановить пароль']" # Новый локатор

    # Личный кабинет
    LOGOUT_BUTTON = "//button[text()='Выход']"
    PROFILE_LINK = "//a[@href='/account/profile']"

    # Конструктор
    BUNS_TAB = "//span[text()='Булки']"
    SAUCES_TAB = "//span[text()='Соусы']"
    FILLINGS_TAB = "//span[text()='Начинки']"
   
    
    # Дополнительные локаторы
    ORDER_IN_PROGRESS_MESSAGE = "//*[contains(text(), 'Ваш заказ начали готовить')]" 