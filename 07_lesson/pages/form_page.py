# Цель: написать автотест для проверки функциональности интернет-магазина на сайте https://www.saucedemo.com/, используя паттерн Page Object.
# Шаги:
# Создание класса Page Object:
# Создать класс для страницы авторизации, который будет содержать методы для ввода логина и пароля, а также для нажатия кнопки входа.
# Создать класс для главной страницы магазина, который будет содержать методы для добавления товаров в корзину и перехода в корзину.
# Создать класс для страницы корзины, который будет содержать методы для нажатия кнопки Checkout и проверки содержимого корзины.
# Создать класс для страницы оформления заказа, который будет содержать методы для заполнения формы данными (имя, фамилия, почтовый индекс) и проверки итоговой стоимости.
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
  def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(driver, 5)

  def add_product_1(self, value):
      self.driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack").click()

  def add_product_2(self, value):
      self.driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-bolt-t-shirt").click()

  def add_product_3(self, value):
      self.driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-onesie").click()

  def jump_card(self):
      self.driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()



