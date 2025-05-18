from Lesson7.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class InventoryPage(BasePage):
    BACKPACK_ADD_BUTTON = (By.ID, 'add-to-cart-sauce-labs-backpack')
    BOLT_T_SHIRT_ADD_BUTTON = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    ONESIE_ADD_BUTTON = (By.ID, 'add-to-cart-sauce-labs-onesie')
    SHOPPING_CART_LINK = (By.CLASS_NAME, 'shopping_cart_link')

    def add_backpack_to_cart(self):
        self.click(self.BACKPACK_ADD_BUTTON)

    def add_bolt_t_shirt_to_cart(self):
        self.click(self.BOLT_T_SHIRT_ADD_BUTTON)

    def add_onesie_to_cart(self):
        self.click(self.ONESIE_ADD_BUTTON)

    def open_cart(self):
        self.click(self.SHOPPING_CART_LINK)