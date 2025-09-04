# Поле ввода
# Открыть браузер FireFox.
# Перейти на страницу: http://the-internet.herokuapp.com/inputs.
# Ввести в поле текст Sky.
# Очистить это поле (метод clear() ).
# Ввести в поле текст Pro.
# Закрыть браузер (метод quit()).

from time import sleep
from selenium import webdriver
# from webdriver_manager.firefox import FirefoxDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()

# зайти на страницу
driver.get("http://the-internet.herokuapp.com/inputs")

search_input = driver.find_element(By.TAG_NAME, "input")
search_input.send_keys("Sky")

sleep(2)

search_input.clear()
search_input.send_keys("Pro")

sleep(2)

driver.quit()