from selenium import webdriver
from selenium.webdriver.common.by import By

def test_standard_user():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.CSS_SELECTOR, "input#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "input#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "input#login-button").click()
    driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
    driver.find_element(By.CSS_SELECTOR, "button#checkout").click()
    driver.find_element(By.CSS_SELECTOR, "input#first-name").send_keys("Svetlana")
    driver.find_element(By.CSS_SELECTOR, "input#last-name").send_keys("Star")
    driver.find_element(By.CSS_SELECTOR, "input#postal-code").send_keys("184600")
    driver.find_element(By.CSS_SELECTOR, "input#continue").click()
    total = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
    print(total)

    assert total == 'Total: $58.29'

    driver.quit()