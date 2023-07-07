import pytest
from selenium.webdriver.common.by import By
import time

from page_objects.login_page import LoginPage
from utils import util

class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             util.get_data())
    def test_negative_login(self, driver,username,password,expected_error_message):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username, password)
        time.sleep(2)
        # Verify error message
        assert login_page.get_error_message() == expected_error_message


    # @pytest.mark.login
    # @pytest.mark.negative
    def test_negative_username(self, driver):
        # Go to website
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type incorrect username  into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("students")

        # Type incorrect password Password1234 into Password field
        password_locator = driver.find_element(By.XPATH, '//input[@name="password"]')
        password_locator.send_keys("Password1234")

        # Punch Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@id='submit']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify error message
        error_text_locator = driver.find_element(By.ID, 'error')
        assert error_text_locator._is_displayed(), "Error message not displayed"

        # verify error message text
        error_text = error_text_locator.text
        assert error_text == "Your username is invalid!", "Error text doesn't match"

    # @pytest.mark.login
    # @pytest.mark.negative
    def test_negative_password(self, driver):
        # Go to website
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username  into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # Type incorrect password Password1234 into Password field
        password_locator = driver.find_element(By.XPATH, '//input[@name="password"]')
        password_locator.send_keys("Password1234")

        # Punch Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@id='submit']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify error message
        error_text_locator = driver.find_element(By.ID, 'error')
        assert error_text_locator._is_displayed(), "Error message not displayed"

        # verify password invalid message
        error_text = error_text_locator.text
        assert error_text == "Your password is invalid!", "Error text doesn't match"
