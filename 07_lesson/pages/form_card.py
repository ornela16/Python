from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CardPage:
  def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(driver, 5)

  def get_open(self):
    self.driver.get("https://www.saucedemo.com/cart.html")

  # def counter_card(self):
  #   txt = self.driver.find_element(By.CSS_SELECTOR, "span.shopping-cart-badge").text
  #   assert int(txt) == "3"

  def click_checkout(self):
    self.driver.find_element(By.CSS_SELECTOR, "button#checkout").click()