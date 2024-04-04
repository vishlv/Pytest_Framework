import datetime
import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class commonfunctions:
    calender_element_xpath = '//div[@class="rd-date"]'
    calender_back_btn_class = "ixi-icon-arrow u-rotate-180 rd-back"
    calender_month_label = '(//div[@class="rd-date"]/div[@class="rd-month"]/div)[1]'

    def __init__(self, driver):
        self.driver = driver

    def element_visibility_check(self, web_element):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of(web_element))
        return ele

    def select_date_for_one_way_journey(self):
        current_date = datetime.date.today().strftime("%B %Y")
        date_arry = current_date.split(" ")
        self.driver.find_element_by_xpath(self.calender_element_xpath)

    def wait_for_station_list(self, element):
        wait = WebDriverWait(self.driver, 10)
        ele = wait.until(EC.visibility_of_element_located(element))
        return ele

    def select_place_for_journey(self, place, locator_for_input):
        element = self.driver.find_element(By.XPATH, locator_for_input)
        element.click()
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(place)
        time.sleep(1)
        element.send_keys(Keys.ENTER)
        # ele = self.driver.find_element(By.XPATH, locator_for_autocomplete)
        # obj = commonfunctions(self.driver)
        # obj.element_visibility_check(ele)
        # action = ActionChains(self.driver)
        # action.move_to_element(ele).click().perform()
