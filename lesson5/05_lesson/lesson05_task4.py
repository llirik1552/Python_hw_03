from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# Создаем экземпляр браузера Firefox
driver = webdriver.Firefox()

try:
    # Переходим на страницу авторизации
    driver.get("http://the-internet.herokuapp.com/login")

    # Находим поле username и вводим значение
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    # Находим поле password и вводим значение
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")

    # Находим кнопку Login и нажимаем на нее
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    # Ждем немного, чтобы страница успела загрузиться
    time.sleep(2)

    # Находим текст с зеленой плашки и выводим его в консоль
    success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
    print(success_message.text)

finally:
    # Закрываем браузер
    driver.quit()