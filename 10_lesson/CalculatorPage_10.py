import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Калькулятор")
class CalculatorPage:
    """
    Это класс для работы со страницей калькулятора
    """
    def __init__(self, driver):
        """
        Эта функция принимает параметры драйвера, открывает страницу сайта в полноэкранном режиме,
        устанавливает время ожидания элемента на странице
        :param driver:  WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 50)

    @allure.step("Открытие страницы калькулятора")
    def open(self):
        """
        Эта функция открывает страницу калькулятора
        :return:  None
        """
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установка задержки {value} секунд")
    def set_delay(self, value):
        """
        Эта функция Устанавливает задержку для выполнения операции на калькуляторе.
        :param value: int — время задержки в секундах.
        """
        self.driver.find_element(By.ID, "delay").clear()
        self.driver.find_element(By.ID, "delay").send_keys(value)

    @allure.step("Нажатие кнопки '7'")
    def set_number7(self):
        """
        Эта функция нажимает на кнопку калькулятора с цифрой '7'
        :return: str — текст на кнопке, которую нужно нажать.
        """
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()

    @allure.step("Нажатие кнопки '8'")
    def set_number8(self):
        """
        Эта функция нажимает на кнопку калькулятора с цифрой '8'
        :return: str — текст на кнопке, которую нужно нажать.
        """
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()

    @allure.step("Нажатие кнопки '+'")
    def set_operator(self):
        """
        Эта функция нажатия на кнопку калькулятора со знаком арифметического действия '+'
        :return: str — текст на кнопке, которую нужно нажать.
        """
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()

    @allure.step("Нажатие кнопки '='")
    def set_equal(self):
        """
        Эта функция нажатия на кнопку калькулятора со знаком '='
        :return: =
        """
        self.driver.find_element(By.CSS_SELECTOR, "span.btn.btn-outline-warning").click()

    @allure.step("Получение результата с экрана калькулятора")
    def result(self, value):
        """
        Эта функция ожидания и получения результата на экране калькулятора.
        :param value: результат - число
        :return: str — текст результата на экране калькулятора.
        """

        self.wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), value))
        return self.driver.find_element(By.CSS_SELECTOR, "div.screen").text