from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="drivers/geckodriver")
driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
time.sleep(3)

user_email = driver.find_element_by_class_name("form-control")
user_password = driver.find_element_by_class_name("textinput")
user_button = driver.find_element_by_class_name("btn")

user_email.send_keys("email_test@email.com")
time.sleep(3)

user_password.send_keys("test01")
time.sleep(3)

user_button.click()
time.sleep(3)

driver.quit()

