from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="drivers/geckodriver")
driver.maximize_window()
driver.get("https://www.w3schools.com/howto/howto_html_file_upload_button.asp")

file_upload_button = driver.find_element_by_id("myFile")
file_upload_button.send_keys("/home/fabri/Escritorio/cat.jpg")
time.sleep(3)

driver.quit()
