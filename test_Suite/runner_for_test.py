import pytest
from pytest_Selenium_framework.test_Cases import goibibo_homePage_test
from pytest_Selenium_framework.test_Cases.ixigo_train_search_test import ixigo_train_search_test


# def test_verify_homepage_title():
#     goibibo_homePage_test.verify_page_title()


def test_trains_page():
    ixigo_train_search_test().search_train_from_mumbai_to_gorakhpur()




