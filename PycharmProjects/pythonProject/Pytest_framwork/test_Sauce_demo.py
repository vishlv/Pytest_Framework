import webdriver_manager.chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


# use of fixtures

global driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# def setup_module(module):
#     driver.implicitly_wait(10)
#     driver.get("https://www.saucedemo.com/")
#
# def teardown_module(modeule):
#     driver.quit()

@pytest.fixture(scope='module')
def init_driver():
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")

    yield
    driver.quit()

@pytest.fixture(scope='class')
def chrm_drv(self,ch_drv):
    self.ch_drv = webdriver.Chrome(ChromeDriverManager().install())


    yield
    ch_drv.close()


@pytest.mark.usefixtures("init_driver")
def test_title():
    assert driver.title,"Swag Labs"

