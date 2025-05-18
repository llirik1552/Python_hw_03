from Lesson7.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutStepOnePage(BasePage):
    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    ZIPCODE_INPUT = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')

    def fill_checkout_data(self, first_name, last_name, zipcode):
        self.input_text(self.FIRST_NAME_INPUT, first_name)
        self.input_text(self.LAST_NAME_INPUT, last_name)
        self.input_text(self.ZIPCODE_INPUT, zipcode)
        self.click(self.CONTINUE_BUTTON)