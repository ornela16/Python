import pytest
import allure
from selenium import webdriver
from sqlalchemy import values

from CalculatorPage_10 import CalculatorPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()

@pytest.mark.parametrize(
    "num1, operation, num2, result, delay",
    [
        ("7", "+", "8", "15", 15),
    ],
)


@allure.title("Тестирование калькулятора: {num1} {operation} {num2} "
              "= {expected_result}")
@allure.description("Тест проверяет корректность работу калькулятора "
                    "с операцией сложения при задержке вывода результата.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(driver, num1, operation,
                         num2, result, delay):
    """
    Тест проверяет работу калькулятора с различными операциями.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    :param num1: str — первое число для операции.
    :param operation: str — операция (+, -, x, ÷).
    :param num2: str — второе число для операции.
    :param result: str — ожидаемый результат операции.
    :param delay: int — задержка в секундах для выполнения операции.
    """
    page = CalculatorPage(driver)

    with allure.step("Открытие страницы калькулятора"):
        page.open()

    with allure.step(f"Установка задержки {delay} секунд"):
        page.set_delay(45)

    with allure.step(f"Нажатие кнопки: {num1}"):
        page.set_number7()

    with allure.step(f"Нажатие кнопки: {operation}"):
        page.set_operator()

    with allure.step(f"Нажатие кнопки: {num2}"):
        page.set_number8()

    with allure.step(f"Нажатие кнопки: '='"):
        page.set_equal()

    with allure.step(f"Ожидание результата {result}"):
         result = page.result("15")
    assert result == "15"