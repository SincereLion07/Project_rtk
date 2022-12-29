import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AuthPage(BasePage):

    MOB_PHONE = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOG_IN = (By.ID, "kc-login")
    EMAIL = (By.ID, "username")
    LOGIN =