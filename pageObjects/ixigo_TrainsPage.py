import time
from selenium.webdriver.common.by import By
from utility.common_functions import Commonfunctions


class Ixigo_TrainPage(Commonfunctions):
    book_trains_options_xpath = '//span[text()="Book Trains"]'
    journey_from_input_xpath = '//input[@placeholder="Leaving from"]'  # '//div[text()="From"]/../../input'
    journey_to_input_xpath = '//input[@placeholder="Going to"]'
    journey_date_input_xpath = '//div[text()="Date"]/../../input'
    calender_container_class = 'rd-container train-cal rd-container-attachment'
    journey_autocomplete = '//div[@class="autocompleter-scroll-cntr"]/div[@data-acindex="0" and text()="Thane (TNA)"]'
    journey_autocomplete_to = '//div[@class="result-row train-station u-box-result selected"]'
    search_button = "//div[@class='form-fields']//button[text()='Search']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def select_book_train_option_xpath(self):
        return self.driver.find_element(By.XPATH, self.book_trains_options_xpath)

    def select_journey_details(self):
        obj = Commonfunctions(self.driver)
        time.sleep(2)
        obj.select_place_for_journey("Thane", self.journey_from_input_xpath)
        obj.select_place_for_journey("Gorakhpur", self.journey_to_input_xpath)

    def click_search_button_xpath(self):
        element = self.driver.find_element(By.XPATH, self.search_button)
        element.click()
