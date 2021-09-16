from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="drivers/geckodriver")
driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")

checkbox = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/input[1]")
time.sleep(3)

print(checkbox.is_displayed())
print(checkbox.is_enabled())
print(checkbox.is_selected())

driver.quit()
