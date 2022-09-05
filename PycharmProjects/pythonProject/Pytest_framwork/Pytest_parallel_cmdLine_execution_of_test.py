from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Test Name should start with test or end with test
# to execute test parallely use command py.test "--test-file-path--" -n (num of parallel execution e.g - 1,2,3,4)

driver = webdriver.Chrome(ChromeDriverManager().install())


def test_launch_YouTube():
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    assert driver.title, "Youtube"


def test_FLipkart():
    driver.get("https:www.flipkart.com")
    assert driver.title, "Youtube"


def test_close_all_browser():
    driver.quit()
