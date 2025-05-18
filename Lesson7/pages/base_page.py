from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        print(f"Waiting for presence of element: {locator}")  # отладка
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))

    def wait_for_visible(self, locator):
        print(f"Waiting for visible element: {locator}")  # отладка
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))

    def wait_until_clickable(self, locator):
        print(f"Waiting for clickable element: {locator}")  # отладка
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text
