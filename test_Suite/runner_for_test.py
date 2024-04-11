from pageObjects.ixigo_TrainsPage import Ixigo_TrainPage
from utility.setupp import Setup


def test_search_train_from_mumbai_to_gorakhpur():
    setup_driver = Setup("https://www.ixigo.com/trains").setup_website()
    trainPage = Ixigo_TrainPage(setup_driver)
    trainPage.select_journey_details()
