# locators.py

class StellarBurgersLocators:
    # ---------- Главная страница (/) ----------
    REGISTER_BUTTON = "//button[text()='Зарегистрироваться']"
    LOGIN_BUTTON_MAIN = "//button[text()='Войти в аккаунт']"
    CONSTRUCTOR_LINK = "//a[@href='/']"
    ACCOUNT_LINK = "//a[@href='/account']"

    # ---------- Страница регистрации (/register) ----------
    REGISTRATION_FORM = "//form"
    NAME_INPUT = "//input[@name='name']"
    EMAIL_INPUT = "//label[text()='Email']/following::input[@name='name']" # TODO: Путь исправлен для корректной работы проверок
    PASSWORD_INPUT = "//input[@name='Пароль']"
    REGISTER_SUBMIT_BUTTON = "//button[text()='Зарегистрироваться']"
    ERROR_MESSAGE = "//p[contains(@class, 'input__error')]"
    # Локатор для ссылки "Войти" на странице регистрации
    LOGIN_LINK_IN_REGISTRATION_FORM = "//a[text()='Войти']"

    # ---------- Страница входа (/login) ----------
    LOGIN_EMAIL_INPUT = "//label[text()='Email']/following::input[@name='name']" # TODO: Путь исправлен для корректной работы проверок
    LOGIN_PASSWORD_INPUT = "//input[@name='Пароль']"
    LOGIN_SUBMIT_BUTTON = "//button[text()='Войти']"
    # Локатор для ссылки "Восстановить пароль"
    FORGOT_PASSWORD_LINK = "//a[text()='Восстановить пароль']"

    # ---------- Страница восстановления пароля (/forgot-password) ----------
    # Локатор для ссылки "Войти" на странице восстановления пароля
    LOGIN_LINK_IN_FORGOT_PASSWORD_FORM = "//a[text()='Войти']"

    # ---------- Личный кабинет (/account) ----------
    LOGOUT_BUTTON = "//button[text()='Выход']"
    PROFILE_LINK = "//a[@href='/account/profile']"

    # ---------- Конструктор (Главная страница, разделы ингредиентов) ----------
    BUNS_TAB = "//span[text()='Булки']/parent::*" # TODO: Путь исправлен для корректной работы проверок
    SAUCES_TAB = "//span[text()='Соусы']/parent::*" # TODO: Путь исправлен для корректной работы проверок
    FILLINGS_TAB = "//span[text()='Начинки']/parent::*" # TODO: Путь исправлен для корректной работы проверок

    # ---------- Дополнительные локаторы ----------
    # Сообщение, которое появляется после регистрации
    ORDER_IN_PROGRESS_MESSAGE = "//*[contains(text(), 'Ваш заказ начали готовить')]"
    # Идентификатор заказа (если нужно проверить его наличие)
    ORDER_NUMBER = "//p[@class='undefined']//following-sibling::h2"