from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="drivers/geckodriver")
driver.maximize_window()
driver.get("https://www.google.com")
time.sleep(3)

driver.execute_script("window.open();")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.google.com")
time.sleep(3)

driver.get("https://www.fb.com")
time.sleep(3)

driver.execute_script("window.open();")
driver.switch_to.window(driver.window_handles[2])
driver.get("https://www.google.com")

time.sleep(3)

driver.get("https://www.youtube.com")
driver.back()

time.sleep(3)

driver.switch_to.window(driver.window_handles[1])
driver.back()

time.sleep(3)

driver.switch_to.window(driver.window_handles[0])
driver.close()

time.sleep(3)

driver.switch_to.window(driver.window_handles[0])
driver.close()

driver.switch_to.window(driver.window_handles[0])
driver.forward()

time.sleep(3)

driver.quit()



