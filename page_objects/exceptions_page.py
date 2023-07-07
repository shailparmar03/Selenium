from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class ExceptionsPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_btn = (By.ID, "add_btn")
    __row1_input = (By.XPATH, '//div[@id ="row1"]/input')
    __row2_input = (By.XPATH, '//div[@id ="row2"]/input')
    __row1_save_btn = (By.XPATH, '//div[@id="row1"]/button[@id="save_btn"]')
    __row2_save_btn = (By.XPATH, '//div[@id="row2"]/button[@id="save_btn"]')
    __confirmation = (By.ID, "confirmation")
    __row1_edit_btn = (By.ID, "edit_btn")
    __instructions = (By.XPATH, '//p[@id="instructions"]')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def add_second_row(self):
        super()._click(self.__add_btn)
        super()._wait_until_element_is_visible(self.__row2_input)

    def is_row2_displayed(self)-> bool:
        return super()._is_displayed(self.__row2_input)

    def add_second_food(self, food: str):
        super()._type(self.__row2_input,food)
        super()._click(self.__row2_save_btn)
        super()._wait_until_element_is_visible(self.__confirmation)

    def get_confirmation_message(self)->str:
        return super()._get_text(self.__confirmation)

    def modify_row1_input(self,food: str):
        super()._click(self.__row1_edit_btn)
        super()._wait_until_element_is_clickable(self.__row1_input)
        super()._clear(self.__row1_input)
        super()._type(self.__row1_input, food)
        super()._click(self.__row1_save_btn)
        super()._wait_until_element_is_visible(self.__confirmation)

    def instructions_are_present(self)->bool:
        return super()._is_displayed(self.__instructions)
