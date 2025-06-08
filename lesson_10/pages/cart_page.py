from lesson_10.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, 'checkout')

    @allure.step("Перейти к оформлению заказа")
    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
