from lesson_10.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

    @allure.title("Ввести логин {username} и пароль {password}")
    def login(self, username, password):
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
