import time

from pytest_Selenium_framework.pageObjects.ixigo_TrainsPage import Ixigo_TrainPage
from pytest_Selenium_framework.utility.setupp import Setup
from selenium import webdriver

class ixigo_train_search_test(Ixigo_TrainPage):

    def __init__(self,):
        driver_obj = Setup("https://www.ixigo.com/trains").setup_website()
        super().__init__(driver_obj)

    def search_train_from_mumbai_to_gorakhpur(self):
        trains = Ixigo_TrainPage(self.driver)
        trains.select_book_train_option_xpath().click()
        trains.select_journey_details()
        # trains.setJourneyTo_xpath().click()
        # trains.setJourneyTo_xpath().send_keys("Gorakhpur")
        # trains.click_search_button_xpath().click()
        time.sleep(5)
