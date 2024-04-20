import datetime
import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Commonfunctions:
    calender_element_xpath = '//div[@class="rd-date"]'
    calender_back_btn_class = "ixi-icon-arrow u-rotate-180 rd-back"
    calender_month_label = '(//div[@class="rd-date"]/div[@class="rd-month"]/div)[1]'

    def __init__(self, driver):
        self.driver = driver

    def element_visibility_check(self, web_element):
        WebDriverWait(self.driver, 10).until(EC.visibility_of(web_element))

    def select_date_for_one_way_journey(self,day, user_input_month_year):
        month_year = str(user_input_month_year)
        month_dict = {'January':'01','February':'02','March':'03','April':'04',
                      'May':'05','June':'06','July':'07','August':'08'
                        ,'September':'09','October':'10','November':'11','December':'12'}
        month_element = self.driver.find_element(By.XPATH, "(//div[@class='rd-month-label'])[1]")
        self.element_visibility_check(month_element)
        next_btn = self.driver.find_element(By.XPATH, "//button[@class='ixi-icon-arrow rd-next']")
        while month_element.text != month_year:
            EC.element_to_be_clickable(next_btn)
            next_btn.click()
        month_year_string = user_input_month_year.split(" ")
        month = month_dict[month_year_string[0]]
        year = month_year_string[1]
        day_element = self.driver.find_element(By.XPATH,
                                               "//td[@data-date='"+day+month+year+"']")
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(day_element))
        day_element.click()


    def wait_for_station_list(self, element):
        wait = WebDriverWait(self.driver, 10)
        ele = wait.until(EC.visibility_of_element_located(element))
        return ele

    def select_place_for_journey(self, place, locator_for_input):
        element = self.driver.find_element(By.XPATH, locator_for_input)
        self.element_visibility_check(element)
        element.click()
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(place)
        time.sleep(1)
        element.send_keys(Keys.ENTER)
