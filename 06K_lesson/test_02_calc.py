import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.usefixtures("driver")
def test_fill_form(driver):
    driver.get("https://bonigarcia.dev/selenium-"
               "webdriver-java/slow-calculator.html")
    element = driver.find_element(By.CSS_SELECTOR, "#delay")
    element.clear()
    driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()
    time.sleep(45)

    result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert int(result) == 15
