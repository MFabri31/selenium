from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="drivers/geckodriver")
driver.maximize_window()
time.sleep(3)

driver.get("https://www.udemy.com/")
time.sleep(3)

# abre una nueva pestaña 
driver.execute_script("window.open('');")

# cambia de pestaña
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
time.sleep(3)

driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

driver.close()
time.sleep(3)

driver.quit()

