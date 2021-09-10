from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="drivers/geckodriver")
driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
time.sleep(3)

forgot_password_link = driver.find_element_by_partial_link_text("¿Has olvidado")
time.sleep(3)

forgot_password_link.click()
time.sleep(3)

user_email = driver.find_element_by_id("form-element--1")
button = driver.find_element_by_class_name("btn")
#validate = driver.find_element_by_class_name("recaptcha-checkbox-border")

user_email.send_keys("email_test@email.com")
time.sleep(3)

#validate.click()
time.sleep(3)

button.click()

driver.quit()