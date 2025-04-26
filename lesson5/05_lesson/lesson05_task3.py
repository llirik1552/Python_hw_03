from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Открываем браузер Firefox
driver = webdriver.Firefox()

try:
    # Переходим на указанную страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Находим поле ввода по его XPath
    input_field = driver.find_element(By.XPATH, "//input[@type='number']")

    # Вводим текст "Sky"
    input_field.send_keys("Sky")

    # Ждем немного, чтобы увидеть введенный текст (опционально)
    time.sleep(2)

    # Очищаем поле ввода
    input_field.clear()

    # Вводим текст "Pro"
    input_field.send_keys("Pro")

    # Ждем немного, чтобы увидеть введенный текст (опционально)
    time.sleep(2)

finally:
    # Закрываем браузер
    driver.quit()