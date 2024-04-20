import time

from selenium.webdriver.common.by import By

from utility.common_functions import Commonfunctions


class Search_resultpage(Commonfunctions):
    serachpage_date_css = 'div.form-cntr.train'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def validate_searchbar_is_loaded(self):
        date_section_element = self.driver.find_element(By.CSS_SELECTOR, self.serachpage_date_css)
        cf = Commonfunctions(self.driver)
        cf.element_visibility_check(date_section_element)
        time.sleep(3)
        self.driver.save_screenshot('test.png')
        print("Result page is loaded")
