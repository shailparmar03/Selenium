import pytest
from page_objects.login_page import LoginPage
from page_objects.login_successful import LoggedInSuccessfullyPage
from utils.myconfigparser import *


class TestPositiveScenarios:
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(get_correct_username(), get_correct_password())
        logged_in_page = LoggedInSuccessfullyPage(driver)
        assert logged_in_page.expected_url in login_page.current_url, "actual url is not same as expected"
        assert logged_in_page.header == get_logged_in_page_header()
        assert logged_in_page.is_logout_button_displayed(), "Logout button should be visible"

