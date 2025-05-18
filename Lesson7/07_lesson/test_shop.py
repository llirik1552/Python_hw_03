import pytest
from Lesson7.pages.login_page import LoginPage
from Lesson7.pages.inventory_page import InventoryPage
from Lesson7.pages.cart_page import CartPage
from Lesson7.pages.checkout_step_one_page import CheckoutStepOnePage
from Lesson7.pages.checkout_overview_page import CheckoutOverviewPage


@pytest.mark.usefixtures("browser")
def test_shop_flow(browser):
    # Открываем главную страницу
    browser.get("https://www.saucedemo.com/")

    # Авторизация
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")
    # Главная страница магазина
    inventory_page = InventoryPage(browser)
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bolt_t_shirt_to_cart()
    inventory_page.add_onesie_to_cart()
    inventory_page.open_cart()

    # Перейдем в корзину
    cart_page = CartPage(browser)
    cart_page.proceed_to_checkout()

    # Заполнять данные для оформления заказа
    checkout_step_one_page = CheckoutStepOnePage(browser)
    checkout_step_one_page.fill_checkout_data("Кирилл", "Кириченко", "12345")

    # Подтверждение заказа
    overview_page = CheckoutOverviewPage(browser)
    total_amount = overview_page.get_total_amount().split(":")[-1].strip()

    # Проверка итоговой суммы
    assert total_amount == "$58.29", (f"Ожидалось $58.29, получено "
                                      f"{total_amount}")
