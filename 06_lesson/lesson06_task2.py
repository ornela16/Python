# Переименовать кнопку
# Напишите скрипт.
#
# Шаги:
# Перейдите на сайт http://uitestingplayground.com/textinput.
# Укажите в поле ввода текст SkyPro.
# Нажмите на синюю кнопку.
# Получите текст кнопки и выведите в консоль ("SkyPro")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://uitestingplayground.com/textinput")

search_input = driver.find_element(By.TAG_NAME, "input")
search_input.send_keys("SkyPro")

driver.find_element(By.ID, "updatingButton").click()

search_input = driver.find_element(By.CLASS_NAME, "btn.btn-primary").text
print(search_input)

driver.quit()