from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="drivers/geckodriver")
driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
time.sleep(3)

user_email = driver.find_element_by_id("email--1")
user_pass = driver.find_element_by_id("id_password")
button_submit = driver.find_element_by_id("submit-id-submit")

user_email.send_keys("email_test@email.com")
time.sleep(3)

user_pass.send_keys("test01")
time.sleep(3)

button_submit.click()
time.sleep(3)

driver.quit()