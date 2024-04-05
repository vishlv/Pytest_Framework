import pytest

from test_Cases.ixigo_train_search_test import ixigo_train_search_test


def test_trains_page():
    ixigo_train_search_test().search_train_from_mumbai_to_gorakhpur()
