from Lesson7.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutOverviewPage(BasePage):
    TOTAL_AMOUNT_LOCATOR = (By.CLASS_NAME, 'summary_total_label')

    def get_total_amount(self):
        return self.get_text(self.TOTAL_AMOUNT_LOCATOR)
