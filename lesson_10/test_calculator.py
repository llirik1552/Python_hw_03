import pytest, time, allure
from selenium import webdriver
from lesson_10.pages.calculator_page import CalculatorPage


@allure.epic("Калькулятор")
@allure.severity("blocker")
@allure.story("Работа с калькулятором")
@allure.title("Работа с положительными числами")
@allure.description("Ввод произвольных чисел, ввод задержки,"
                    " ожидание результата")
@allure.feature("Работа без включения VPN")
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.story("Запуск теста")
def test_calculator_functionality(driver):
    calculator = CalculatorPage(driver)
    calculator.open(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    calculator.set_delay(45)

    with allure.step("Очищаем результат (если нужно)"):
        calculator.click_button("C")

    with allure.step("Вводим данные"):
        calculator.click_button("7")
        calculator.click_button("+")
        calculator.click_button("8")
        calculator.click_button("=")

    with allure.step("Ожидаем"):
        start_time = time.time()
        result = calculator.get_result()
        end_time = time.time()

    with allure.step("Получаем результат"):
        assert result == "15", f"Expected result '15', but got '{result}'"
        assert 45 <= (end_time - start_time) <= 50, (
        f"Calculation took {end_time - start_time:.1f} seconds, expected 45-50"
    )
