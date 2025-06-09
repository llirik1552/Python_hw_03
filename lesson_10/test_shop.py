import allure, pytest
from lesson_10.pages.login_page import LoginPage
from lesson_10.pages.inventory_page import InventoryPage
from lesson_10.pages.cart_page import CartPage
from lesson_10.pages.checkout_step_one_page import CheckoutStepOnePage
from lesson_10.pages.checkout_overview_page import CheckoutOverviewPage


@allure.epic("Интернет магазин")
@allure.severity("blocker")
@allure.story("Работа с магазином")
@allure.title("Работа с сайтом магазина покупок")
@allure.description("Выбор покупок из списка и проверка их наличия в корзине")
@allure.feature("Работа без включения VPN")
def test_shop_flow(browser):
    with allure.step("Открываем главную страницу"):
        browser.get("https://www.saucedemo.com/")

    with allure.step("Авторизация"):
        login_page = LoginPage(browser)
        login_page.login("standard_user", "secret_sauce")
    with allure.step("Главная страница магазина"):
        inventory_page = InventoryPage(browser)
        inventory_page.add_backpack_to_cart()
        inventory_page.add_bolt_t_shirt_to_cart()
        inventory_page.add_onesie_to_cart()
        inventory_page.open_cart()

    with allure.step("Перейдем в корзину"):
        cart_page = CartPage(browser)
        cart_page.proceed_to_checkout()

    with allure.step("Заполнять данные для оформления заказа"):
        checkout_step_one_page = CheckoutStepOnePage(browser)
        checkout_step_one_page.fill_checkout_data("Кирилл",
                                                  "Кириченко", "12345")
    with allure.step("Подтверждение заказа"):
         overview_page = CheckoutOverviewPage(browser)
         total_amount = overview_page.get_total_amount().split(":")[-1].strip()

    with allure.step("Проверка итоговой суммы"):
        assert total_amount == "$58.29", (f"Ожидалось $58.29, получено "
                                      f"{total_amount}")
