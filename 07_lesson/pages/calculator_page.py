from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
  def __init__(self, driver):
    self.driver = driver
    self.driver.implicitly_wait(4)
    self.driver.maximize_window()

  def open(self):
    self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

  def set_delay(self, value,):
    self.driver.find_element(By.ID, "delay").clear()
    self.driver.find_element(By.ID, "delay").send_keys(value)

  def set_number7(self, value):
    self.driver.find_element(By.XPATH, "//span[text()='7']").click()

  def set_number8(self, value):
    self.driver.find_element(By.XPATH, "//span[text()='8']").click()

  def set_operator(self, value):
    self. driver.find_element(By.XPATH, "//span[text()='+']").click()

  def set_equal(self, value):
    self.driver.find_element(By.CSS_SELECTOR, "span.btn.btn-outline-warning").click()

  def result(self, value):

    self.wait = WebDriverWait(self.driver, 50)
    self.wait.until(
      EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "value"))

    return  self.driver.find_element(By.CSS_SELECTOR, "div.screen").text
