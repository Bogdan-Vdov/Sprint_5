# conftest.py или просто helpers.py (без pytest)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    """Функция для инициализации драйвера Chrome"""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver

# Если хочешь использовать как контекстный менеджер (опционально):
from contextlib import contextmanager

@contextmanager
def get_driver_context():
    """Контекстный менеджер для инициализации и закрытия драйвера"""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    try:
        yield driver
    finally:
        driver.quit()