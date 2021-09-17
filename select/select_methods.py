from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox(executable_path="drivers/geckodriver")
driver.maximize_window()
driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")

menu = Select(driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select"))
time.sleep(3)

menu.select_by_index(10)
time.sleep(3)

menu.select_by_value("5")
time.sleep(3)

menu.select_by_visible_text("Audi")
time.sleep(3)

driver.quit()