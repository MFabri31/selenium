from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
import time

class Select(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="drivers/geckodriver")
        self.driver.maximize_window()


    def test_select_options(self):
        self.driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")

        menu = Select(self.driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select"))
        time.sleep(3)

        menu.select_by_index(10)
        time.sleep(3)

        menu.select_by_value("5")
        time.sleep(3)

        menu.select_by_visible_text("Audi")
        time.sleep(3)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
        