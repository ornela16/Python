import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

@allure.feature("Интернет-магазин")
class AuthPage:
  def __init__(self, driver):
    """
    Конструктор класса AuthPage.

    :param driver: WebDriver — объект драйвера Selenium.
    """
    self.driver = driver
    self.wait = WebDriverWait(driver, 5)


  @allure.step("Открытие страницы авторизации пользователя.")
  def open(self):
    """
    Открывает страницу с формой для ввода логина и пароля покупателя.
    """
    self.driver.get("https://www.saucedemo.com")

  @allure.step("Добавление логина пользователя")
  def input_login(self, value):
    """
    Возвращает логин пользователя.

    :return: str — текст в окне формы с данными.
    """
    self.driver.find_element(By.CSS_SELECTOR, "input#user-name").send_keys(value)

  @allure.step("Добавление пароля пользователя")
  def input_password(self, value):
    """
    Возвращает пароль пользователя.

    :return: str — текст в окне формы с данными.
    """
    self.driver.find_element(By.CSS_SELECTOR, "input#password").send_keys(value)

  @allure.step("Нажатие кнопки 'login'")
  def click_login(self):
    """
    Нажимает на кнопку "login" для перехода на страницу каталога товаров.

    """
    self.driver.find_element(By.CSS_SELECTOR, "input#login-button").click()