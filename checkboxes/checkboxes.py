from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="drivers/geckodriver")
driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
time.sleep(3)

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

for check in checkboxes:
    if check.is_displayed is True and check.is_selected is False:
        check.click()
        time.sleep(3)
        
driver.quit()
      

