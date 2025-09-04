# Форма авторизации

# Открыть браузер FireFox.
# Перейти на страницу http://the-internet.herokuapp.com/login.
# В поле username ввести значение tomsmith.
# В поле password ввести значение SuperSecretPassword!.
# Нажать кнопку Login.
# Вывести текст с зеленой плашки в консоль.
# Закрыть браузер (метод quit())

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")

search_input = driver.find_element(By.ID, "username")
search_input.send_keys("tomsmith")

search_input = driver.find_element(By.ID, "password")
search_input.send_keys("SuperSecretPassword!")

driver.find_element(By.CLASS_NAME, "radius").click()

search_input = driver.find_element(By.ID, "flash").text
print(search_input)

driver.quit()

sleep(5)