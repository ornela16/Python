# Нажать на кнопку
# Перейдите на страницу http://uitestingplayground.com/ajax.
# Нажмите на синюю кнопку.
# Получите текст из зеленой плашки.
# Выведите его в консоль
# ("Data loaded with AJAX get request.").

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.implicitly_wait(20)

driver.get("http://uitestingplayground.com/ajax")

bluebutton = "ajaxButton"
driver.find_element(By.ID, bluebutton).click()

id_content = driver.find_element(By.CSS_SELECTOR, "#content")
result = id_content.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(result)

sleep(2)
driver.quit()