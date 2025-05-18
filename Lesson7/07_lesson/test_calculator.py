import pytest
from selenium import webdriver
from Lesson7.pages.calculator_page import CalculatorPage
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator_functionality(driver):
    calculator = CalculatorPage(driver)
    calculator.open(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    calculator.set_delay(45)

    # Очищаем результат (если нужно)
    calculator.click_button("C")

    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")

    start_time = time.time()
    result = calculator.get_result()
    end_time = time.time()

    assert result == "15", f"Expected result '15', but got '{result}'"
    assert 45 <= (end_time - start_time) <= 50, (
        f"Calculation took {end_time - start_time:.1f} seconds, expected 45-50"
    )
