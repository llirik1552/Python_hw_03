from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input_field.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button.click()

button_text = button.text
print(button_text)

driver.quit()