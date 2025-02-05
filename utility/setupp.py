from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Setup:
    def __init__(self, url):
        self.url = url

    def setup_website(self):
        chrome_opt = Options()
        # chrome_opt.add_argument('--headless')
        # chrome_opt.add_argument('--disable-gpu')
        # chrome_opt.binary_location = "D://WebDrivers//chrome-win64//chrome.exe"
        # driver_path = "D://WebDrivers//chromedriver-win64//chromedriver.exe"
        # service = Service(executable_path=driver_path)
        # driver = webdriver.Chrome(service=service, options=chrome_opt)
        # chromedriver_autoinstaller.install()
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_opt)
        driver.delete_all_cookies()
        driver.get(self.url)
        driver.set_page_load_timeout(3000)
        driver.maximize_window()
        return driver
