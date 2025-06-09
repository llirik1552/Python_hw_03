import pytest
from selenium import webdriver
import allure


@allure.epic("Браузер")
@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
