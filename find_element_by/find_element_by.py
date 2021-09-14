from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(executable_path="drivers/geckodriver")
driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2Fjoin%2Flogin-popup%2F%3Flocale%3Des_ES%26response_type%3Dhtml%26next%3Dhttps%253A%252F%252Fwww.udemy.com%252F")

driver.maximize_window()

time.sleep(3)

user_email = driver.find_element(By.ID,"email--1")
user_password = driver.find_element(By.ID,"id_password")
button = driver.find_element(By.ID,"submit-id-submit")

user_email.send_keys("email_test@gmail.com")
time.sleep(3)

user_password.send_keys("test01")
button.click()

time.sleep(3)

driver.quit()