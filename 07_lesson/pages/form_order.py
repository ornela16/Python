from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class OrderPage:
  def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(driver, 15)

  def get_open_order(self):
    self.driver.get("https://www.saucedemo.com/checkout-step-one.html")

  def first_name(self, value):
    self.driver.find_element(By.CSS_SELECTOR, "input#first-name").send_keys(value)

  def last_name(self, value):
    self.driver.find_element(By.CSS_SELECTOR, "input#last-name").send_keys(value)

  def postal_code(self, value):
    self.driver.find_element(By.CSS_SELECTOR, "input#postal-code").send_keys(value)

  def button_continue(self):
    self.driver.find_element(By.CSS_SELECTOR, "input#continue").click()

  def total(self):
    total = self.driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
    return total