from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class AuthPage:
  def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(driver, 5)

  def open(self):
    self.driver.get("https://www.saucedemo.com")

  def input_login(self, value):
    self.driver.find_element(By.CSS_SELECTOR, "input#user-name").send_keys(value)

  def input_password(self, value):
    self.driver.find_element(By.CSS_SELECTOR, "input#password").send_keys(value)

  def click_login(self):
    self.driver.find_element(By.CSS_SELECTOR, "input#login-button").click()