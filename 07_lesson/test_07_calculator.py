import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_calculator(driver):
    driver = webdriver.Chrome()
    page = CalculatorPage(driver)
    page.open()
    page.set_delay(45)
    page.set_number7("7")
    page.set_operator("+")
    page.set_number8("8")
    page.set_equal("=")
    result = page.result("15")
    assert result == "15"