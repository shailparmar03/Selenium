import pytest


from page_objects.exceptions_page import ExceptionsPage


class TestExceptions:
    @pytest.mark.exceptions
    # @pytest.mark.debug
    def test_no_such_element_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert exceptions_page.is_row2_displayed(),"Row 2 isn't displayed"

    @pytest.mark.exceptions
    # @pytest.mark.debug
    def test_element_not_interactable_exception(self, driver):
        # Open page
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        exception_page.add_second_food("tacos")
        assert exception_page.get_confirmation_message() == "Row 2 was saved",\
            "Confirmation message is not as expected"


    # Test case 3: InvalidElementStateException
    @pytest.mark.exceptions
    # @pytest.mark.debug
    def test_invalid_element_state_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.modify_row1_input("tacos")
        assert exceptions_page.get_confirmation_message() == "Row 1 was saved", "Text mismatch"

    # Test case 4: StaleElementReferenceException
    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_stale_element_reference_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        assert exceptions_page.instructions_are_present(), "Instructions not displayed"
        exceptions_page.add_second_row()
        assert not exceptions_page.instructions_are_present(),\
            "instruction text element should not displayed"

    # Test case 5: TimeoutException
    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_timeout_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert exceptions_page.is_row2_displayed(), "second input field isn't displayed"
