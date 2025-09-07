# Дождаться картинки
# Напишите скрипт.
# Шаги:
# Перейдите на сайт https://bonigarcia.dev/selenium-webdriver-java/loading-images.html.
# Дождитесь загрузки всех картинок.
# Получите значение атрибута src  у 3-й картинки.
# Выведите значение в консоль.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(20)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

atribut=driver.find_element(By.CSS_SELECTOR, "img[alt='award']").get_attribute("src")
print(atribut)

sleep(3)
driver.quit()