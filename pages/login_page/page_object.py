import logging

from . import locators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        assert self._is_displayed(locators.PASSWORD_FIELD, timeout=10)
        assert self._is_displayed(locators.USERNAME_FIELD, timeout=10)

    @property
    def log_in_button(self):
        return self._find(locators.LOG_IN_BUTTON)

    @property
    def log_in_error_is_displayed(self):
        return self._is_displayed(locators.LOG_IN_ERROR)

    @property
    def password_field(self):
        return self._find(locators.PASSWORD_FIELD)

    @property
    def username_field(self):
        return self._find(locators.USERNAME_FIELD)

    def click_log_in_button(self):
        logging.info('Clicking "Log In" button.')
        self.log_in_button.click()

    def enter_password(self, password):
        logging.info(f'Entering password of "{password}".')
        self.password_field.send_keys(password)

    def enter_username(self, username):
        logging.info(f'Entering username of "{username}".')
        self.username_field.send_keys(username)

