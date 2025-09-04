# Поле ввода

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/inputs")

search_input = driver.find_element(By.TAG_NAME, "input")
search_input.send_keys("Sky")

sleep(2)

search_input.clear()
search_input.send_keys("Pro")

driver.quit()