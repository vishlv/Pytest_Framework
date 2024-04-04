from selenium import webdriver
class navigation_menu:
    trains_menu_xpath = '//span[text()="Trains"]'
    def __init__(self,driver):
        self.driver = driver

    def select_trains_options(self):
        self.driver.find_element_by_xpath(self.trains_menu_xpath).click()

