import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.usefixtures("driver")
def test_fill_form(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Кирилл")
    driver.find_element(By.ID, "last-name").send_keys("Кириченко")
    driver.find_element(By.ID, "postal-code").send_keys("211334")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    total_cost = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    total_cost_value = float(total_cost.split("$")[1])

    assert total_cost_value == 58.29
