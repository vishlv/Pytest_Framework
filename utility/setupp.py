from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Setup:
    def __init__(self, url):
        self.url = url

    def setup_website(self):
        chrome_opt = Options()
        chrome_opt.binary_location = "D://WebDrivers//chrome-win64//chrome.exe"
        driver_path = "D://WebDrivers//chromedriver-win64//chromedriver.exe"
        driver = webdriver.Chrome(executable_path=driver_path, options=chrome_opt)
        driver.delete_all_cookies()
        driver.get(self.url)
        driver.set_page_load_timeout(3000)
        driver.maximize_window()
        return driver
