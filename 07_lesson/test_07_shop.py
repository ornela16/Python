import pytest
from selenium import webdriver
from pages.form_card import CardPage
from pages.form_page import FormPage
from pages.form_auth import AuthPage
from pages.form_order import OrderPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_form_auth():
    driver = webdriver.Firefox()
    form_page = AuthPage(driver)
    form_page.open()
    form_page.input_login("standard_user")
    form_page.input_password("secret_sauce")
    form_page.click_login()
    form_page = FormPage(driver)
    form_page.add_product_1("Sauce Labs Backpack")
    form_page.add_product_2("Sauce Labs Bolt T-Shirt")
    form_page.add_product_3("Sauce Labs Onesie")
    form_page.jump_card()
    form_page = CardPage(driver)
    form_page.counter_card()
    form_page.click_checkout()
    form_page = OrderPage(driver)
    form_page.first_name("Svetlana")
    form_page.last_name("Star")
    form_page.postal_code( "184600")
    form_page.button_continue()
    total = form_page.total()

    assert total == 'Total: $58.29'