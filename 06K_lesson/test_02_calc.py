import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.usefixtures("driver")
def test_fill_form(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )
    element = driver.find_element(By.CSS_SELECTOR, "#delay")
    element.clear()
    driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()
    WebDriverWait(driver, 46).until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "screen"), "15"))
    result = driver.find_element(By.CLASS_NAME, "screen").text

    result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert int(result) == 15
