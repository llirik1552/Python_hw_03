from lesson_10.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class InventoryPage(BasePage):
    BACKPACK_ADD_BUTTON = (By.ID, 'add-to-cart-sauce-labs-backpack')
    BOLT_T_SHIRT_ADD_BUTTON = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    ONESIE_ADD_BUTTON = (By.ID, 'add-to-cart-sauce-labs-onesie')
    SHOPPING_CART_LINK = (By.CLASS_NAME, 'shopping_cart_link')

    @allure.title("Добавить рюкзак в корзину")
    def add_backpack_to_cart(self):
        self.click(self.BACKPACK_ADD_BUTTON)

    @allure.title("Добавить футболку в корзину")
    def add_bolt_t_shirt_to_cart(self):
        self.click(self.BOLT_T_SHIRT_ADD_BUTTON)

    @allure.title("Добавить комбинезон в корзину")
    def add_onesie_to_cart(self):
        self.click(self.ONESIE_ADD_BUTTON)

    @allure.title("Открыть карту")
    def open_cart(self):
        self.click(self.SHOPPING_CART_LINK)
