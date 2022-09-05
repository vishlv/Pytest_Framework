from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture(scope='class')
def driver_in(request):
    p = ChromeDriverManager()
    web_driver = webdriver.Chrome(executable_path=p.install())
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.mark.usefixtures("driver_in")
class BaseTest:
    pass


class Test_google(BaseTest):
    def test_google_title(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Google"
