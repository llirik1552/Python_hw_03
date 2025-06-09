from lesson_10.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class CheckoutStepOnePage(BasePage):
    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    ZIPCODE_INPUT = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')

    @allure.title("Заполнить данные для оформления "
                  "заказа {first_name} {last_name} {zipcode}")
    def fill_checkout_data(self, first_name, last_name, zipcode):
        self.input_text(self.FIRST_NAME_INPUT, first_name)
        self.input_text(self.LAST_NAME_INPUT, last_name)
        self.input_text(self.ZIPCODE_INPUT, zipcode)
        self.click(self.CONTINUE_BUTTON)
