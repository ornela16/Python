import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


@allure.feature("Интернет-магазин")
class OrderPage:
  """
  Это класс для работы со страницей оформления заказа в интернет-магазине.
  """

  def __init__(self, driver):
    """
     Это конструктор класса OrderPage

     :param driver: WebDriver — объект драйвера Selenium.
     """
    self.driver = driver
    self.wait = WebDriverWait(driver, 15)

  @allure.step("Открытие страницы оформления заказа с формой данных пользователя.")
  def get_open_order(self):
    """
    Открывает страницу с формой для добавления данных покупателя.
    """
    self.driver.get("https://www.saucedemo.com/checkout-step-one.html")

  @allure.step("Добавление имени пользователя")
  def first_name(self, value):
    """
    Возвращает имя пользователя.

    :return: str — текст в окне формы с данными.
    """
    self.driver.find_element(By.CSS_SELECTOR, "input#first-name").send_keys(value)

  @allure.step("Добавление фамилии пользователя")
  def last_name(self, value):
    """
    Возвращает фамилию пользователя.

    :return: str — текст в окне формы с данными.
    """
    self.driver.find_element(By.CSS_SELECTOR, "input#last-name").send_keys(value)


  @allure.step("Добавление почтового индекса адреса пользователя")
  def postal_code(self, value):
    """
    Возвращает значение индекса адреса пользователя.

    :return: str — текст в окне формы с данными.
    """
    self.driver.find_element(By.CSS_SELECTOR, "input#postal-code").send_keys(value)


  @allure.step("Нажатие кнопки: 'continue'")
  def button_continue(self):
    """
    Нажимает на кнопку "Continue" для перехода на следующую страницу.

    """
    self.driver.find_element(By.CSS_SELECTOR, "input#continue").click()


  @allure.step("Получение итоговой стоимости заказа")
  def total(self):
    """
    Возвращает итоговую стоимость товаров в заказе.

    :return: str — текст стоимости на странице заказа.
    """
    total = self.driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
    return total