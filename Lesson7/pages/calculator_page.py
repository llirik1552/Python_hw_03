from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_display = (By.CSS_SELECTOR, ".screen")
        self.button_locator = "//span[text()='{}']"

    def open(self, url):
        self.driver.get(url)

    def set_delay(self, seconds):
        delay_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.delay_input)
        )
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_button(self, button_text):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.button_locator.format(button_text))
            )
        )
        button.click()

    def get_result(self, timeout=50):
        # Ожидаем, пока текст в дисплее изменится на результат (перестанет содержать операторы)
        def result_is_calculated(driver):
            display = driver.find_element(*self.result_display)
            return display.text not in ['', '7+8'] and not any(op in display.text for op in '+-*/')

        WebDriverWait(self.driver, timeout).until(result_is_calculated)
        return self.driver.find_element(*self.result_display).text
