from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

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



