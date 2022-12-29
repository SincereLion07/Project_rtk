import logging
from selenium.common.exceptions import TimeoutException
from typing import Tuple
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebElement


class BasePage:

    LOGGER = logging.getLogger(__name__)
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_page(self):
        try:
            self.browser.get(self.url)
        except Exception as e:
            self.LOGGER.error(f"tException: {e}")

    def page_is_open(self, url):
        try:
            self.wait_for_url_to_be(url)
            return True
        except TimeoutException:
            return False

    def wait_for_url_to_be(self, url: str, timeout: int = 5) -> bool:
        try:
            return WebDriverWait(self.browser, timeout).until(ec.url_to_be(url))
        except TimeoutException as e:
            self.LOGGER.error(f"TimeoutException: {e}")

    def wait_until_clickable(self, locator: Tuple, timeout: int = 5) -> WebElement:
        try:
            return WebDriverWait(self.browser, timeout).until(
                ec.element_to_be_clickable(locator))
        except TimeoutException as e:
            self.LOGGER.error(f"TimeoutException: {e}")

    def wait_until_visible(self, locator: Tuple, timeout: int = 5) -> WebElement:
        try:
            return WebDriverWait(self.browser, timeout).until(
                ec.visibility_of_element_located(locator)
            )
        except TimeoutException as e:
            self.LOGGER.error(f"TimeoutException: {e}")

    def wait_until_alert(self, timeout: int = 5) -> WebElement:
        try:
            return WebDriverWait(self.browser, timeout).until(
                ec.alert_is_present()
            )

        except TimeoutException as e:
            self.LOGGER.error(f"TimeoutException: {e}")

    def wait_until_present(self, locator: Tuple, timeout: int = 5) -> WebElement:
        try:
            return WebDriverWait(self.browser, timeout).until(
                ec.presence_of_element_located(locator)
            )
        except TimeoutException as e:
            self.LOGGER.error(f"TimeoutException: {e}")

    def wait_until_all_present(self, locator: Tuple, timeout: int = 5) -> WebElement:
        try:
            return WebDriverWait(self.browser, timeout).until(
                ec.presence_of_all_elements_located(locator)
            )
        except TimeoutException as e:
            self.LOGGER.error(f"TimeoutException: {e}")

    def element_is_present(self, locator: Tuple, timeout: int = 5) -> bool:
        try:
            self.wait_until_present(locator, timeout)
            return True
        except TimeoutException as e:
            self.LOGGER.error(f"TimeoutException: {e}")

    def go_to_home(self):
        self.wait_until_clickable(self.B_HOME).click()

    def go_to_contact(self):
        self.wait_until_clickable(self.B_CONTACT).click()

    def go_to_cart(self):
        self.wait_until_clickable(self.B_CART).click()

    def go_to_login(self):
        self.wait_until_clickable(self.B_LOGIN).click()

    def go_to_signup(self):
        self.wait_until_clickable(self.B_SIGN_UP).click()
