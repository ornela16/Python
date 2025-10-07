import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

@allure.feature("Интернет-магазин")
class FormPage:

  def __init__(self, driver):
    """
       Конструктор класса FormPage для выбора и добавления товаров в корзину.

       :param driver: WebDriver — объект драйвера Selenium.
    """
    self.driver = driver
    self.wait = WebDriverWait(driver, 5)

  @allure.step("Добавление первого товара в корзину.")
  def add_product_1(self):
      """
      Нажимает на кнопку "Add to cart" для добавления товара в корзину.

      """
      self.driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack").click()

  @allure.step("Добавление второго товара в корзину.")
  def add_product_2(self):
      """
      Нажимает на кнопку "Add to cart" для добавления товара в корзину.

      """
      self.driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-bolt-t-shirt").click()

  @allure.step("Добавление третьего товара в корзину.")
  def add_product_3(self):
      """
      Нажимает на кнопку "Add to cart" для добавления товара в корзину..

      """
      self.driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-onesie").click()

  @allure.step("Нажатие на значок корзины")
  def jump_card(self):
      """
      Нажимает на значок "корзина" для перехода на страницу корзины товаров.

      """
      self.driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()