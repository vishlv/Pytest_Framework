import time

from pageObjects.ixigo_TrainsPage import Ixigo_TrainPage
from pageObjects.search_resultpage import Search_resultpage
from utility.common_functions import Commonfunctions
from utility.setupp import Setup


def test_search_train_from_mumbai_to_gorakhpur():
    setup_driver = Setup("https://www.ixigo.com/trains").setup_website()
    trainPage = Ixigo_TrainPage(setup_driver)
    srp = Search_resultpage(setup_driver)
    cf = Commonfunctions(setup_driver)
    trainPage.select_journey_details()
    cf.select_date_for_one_way_journey('10','July 2024')
    trainPage.click_search_button_xpath()
    srp.validate_searchbar_is_loaded()
