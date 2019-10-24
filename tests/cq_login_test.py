import logging
import pytest

from pages.login_page.page_object import LoginPage


class TestCQLoginPage:
    @pytest.fixture(scope='session')
    def login_page_driver(self, driver):
        log_in_url = 'https://plus.cq.com/login'

        logging.info(f'Navigating to {log_in_url}')
        driver.get(log_in_url)

        return driver

    @pytest.mark.login
    def test_user_sees_error_message_when_attempting_to_log_in_with_invalid_crendentials(self, login_page_driver):
        login_page = LoginPage(login_page_driver)

        logging.info('Verifying that the log in error message is not displayed.')
        assert login_page.log_in_error_is_displayed is False

        login_page.enter_username('this_is_not_a_real_username@email.com')
        login_page.enter_password('this_is_not_a_real_password')

        login_page.click_log_in_button()

        logging.info('Verifying that the log in error message is displayed.')
        assert login_page.log_in_error_is_displayed
