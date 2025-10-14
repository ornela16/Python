import pytest
import allure
from selenium import webdriver
from form_card import CardPage
from form_page import FormPage
from form_auth import AuthPage
from form_shop_order_10 import OrderPage

@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@allure.title("Тестирование оформления заказа на покупку товаров в интернет-магазине")
@allure.description("Тест проверяет: возможность авторизации на сайте, успешность добавления товаров в корзину, "
                    "корректность заполнения формы доставки и оплаты заказа.")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_shop(driver):
    """
    Тест проверяет возможность оформления заказа на сайте интернет-магазина.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    """

    form_page = AuthPage(driver)

    with allure.step("Открытие страницы авторизации"):
        form_page.open()
        form_page.input_login("standard_user")
        form_page.input_password("secret_sauce")

    with allure.step(f"Нажатие кнопки 'login', переход на страницу каталога товаров"):
        form_page.click_login()

    form_page = FormPage(driver)

    with allure.step(f"Нажатие кнопки 'Add to cart' для добавления в корзину первого продукта."):
        form_page.add_product_1()

    with allure.step(f"Нажатие кнопки 'Add to cart' для добавления в корзину второго продукта."):
        form_page.add_product_2()

    with allure.step(f"Нажатие кнопки 'Add to cart' для добавления в корзину третьего продукта."):
        form_page.add_product_3()

    with allure.step("Нажатие на значок 'корзина' для перехода на страницу корзины товаров."):
        form_page.jump_card()

    form_page = CardPage(driver)

    with allure.step("Получение количества товаров в корзине."):
        form_page.counter_card()

    with allure.step(f"Нажатие кнопки 'checkout', переход на страницу оформления заказа"):
        form_page.click_checkout()

    form_page = OrderPage(driver)

    with allure.step("Добавление имени пользователя в форму данных заказа"):
        form_page.first_name("Svetlana")

    with allure.step("Добавление фамилии пользователя в форму данных заказа"):
        form_page.last_name("Star")

    with allure.step("Добавление почтового индекса пользователя в форму данных заказа"):
        form_page.postal_code( "184600")

    with allure.step(f"Нажатие кнопки 'continue', переход на следующую страницу"):
        form_page.button_continue()

    with allure.step("Получение итоговой стоимости заказа"):
        total = form_page.total()

    with allure.step("Проверка результата"):
        assert total == 'Total: $58.29'