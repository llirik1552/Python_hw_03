from Lesson7.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, 'checkout')

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
