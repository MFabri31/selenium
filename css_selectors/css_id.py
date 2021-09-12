from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="drivers/geckodriver")

driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2Fjoin%2Flogin-popup%2F%3Flocale%3Des_ES%26response_type%3Dhtml%26next%3Dhttps%253A%252F%252Fwww.udemy.com%252F")

time.sleep(3)

user_email = driver.find_element_by_css_selector("input#email--1")
user_password = driver.find_element_by_css_selector("input#id_password")
button = driver.find_element_by_css_selector("input#submit-id-submit")

user_email.send_keys("email_test@email.com")
time.sleep(1)

user_password.send_keys("test01")
time.sleep(1)

button.click()

driver.quit()


