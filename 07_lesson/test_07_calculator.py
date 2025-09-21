import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()

def test_calculator(driver):
    page = CalculatorPage(driver)
    page.set_delay(45)
    page.set_number7("7")
    page.set_operator("+")
    page.set_number8("8")
    page.set_equal("=")
    result = page.result("15")
    assert result == "15"