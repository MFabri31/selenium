from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="drivers/geckodriver")
driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")

select = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select")
options = driver.find_elements_by_tag_name("option")

for option in options:
    option.click()
    time.sleep(3)
    
driver.quit()
