import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

@allure.feature("Интернет-магазин")
class CardPage:

  def __init__(self, driver):
    """
     Конструктор класса CardPage для работы со страницей корзины товаров.

     :param driver: WebDriver — объект драйвера Selenium.
     """
    self.driver = driver
    self.wait = WebDriverWait(driver, 5)

  @allure.step("Открытие страницы корзины товаров.")
  def get_open(self):
    """
    Открывает страницу с карточками товаров, выбранных для заказа.
    """
    self.driver.get("https://www.saucedemo.com/cart.html")

  @allure.step("Получение количества товаров в корзине.")
  def counter_card(self):
    """
     Возвращает количество товаров в корзине покупателя.

     :return: str — текст результата на странице корзины.
     """
    txt = self.driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a > span").text
    return txt

  @allure.step("Нажатие кнопки: 'checkout'")
  def click_checkout(self):
    """
    Нажимает на кнопку "checkout" для перехода на следующую страницу.

    """
    self.driver.find_element(By.CSS_SELECTOR, "button#checkout").click()