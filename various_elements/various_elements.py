from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="drivers/geckodriver")
driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2Fjoin%2Flogin-popup%2F%3Flocale%3Des_ES%26response_type%3Dhtml%26next%3Dhttps%253A%252F%252Fwww.udemy.com%252F")
driver.maximize_window()
time.sleep(3)

inputs = driver.find_elements_by_class_name("form-control")

for input in inputs:
    time.sleep(3)
    input.send_keys("test01")

