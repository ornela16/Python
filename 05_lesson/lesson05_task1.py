# Клик по кнопке с CSS-классом

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# зайти на страницу
driver.get(" http://uitestingplayground.com/classattr")

bluebutton = "button.btn.class2.btn-primary.btn-test"
driver.find_element(By.CSS_SELECTOR, bluebutton)

element = driver.find_element(By.CSS_SELECTOR, bluebutton)
element.send_keys("button.btn.class2.btn-primary.btn-test")

element.send_keys(Keys.RETURN)

sleep(20)