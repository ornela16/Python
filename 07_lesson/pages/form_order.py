from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class OrderPage:
  def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(driver, 5)
    self.fields = {
      'First Name' : "Svetlana",
      'Last Name' : "Star",
      'Zip/Postal Code' : "184600"
    }

  def get_open_order(self):
    self.driver.get("https://www.saucedemo.com/checkout-step-one.html")

  def fill_form(self):
    for field, value in self.fields.items():
      self.wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR,field))
      ).send_keys(value)

  def total(self):
    total = self.driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
    print(total)
    assert total == 'Total: $58.29'

  def button_continue(self):
    self.driver.find_element(By.CSS_SELECTOR, "input#continue").click()