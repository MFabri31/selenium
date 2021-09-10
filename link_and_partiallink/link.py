from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="drivers/geckodriver")
driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
time.sleep(3)

forgot_password_link = driver.find_element_by_link_text("¿Has olvidado la contraseña?")
time.sleep(3)

forgot_password_link.click()
time.sleep(3)

driver.quit()