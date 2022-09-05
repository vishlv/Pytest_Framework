import pytest


# start with test keyword or end with test keyword
#to execute test iwth matching tes case name via terminal comand is py.test "---pytest-file---path" -m  "matching_testcase_name"
@pytest.mark.launch_google
def test_open_googel_home_page():
    a = 1
    b = 3
    assert a + 2 == b, "Test Case Passed"

@pytest.mark.test2
def test_2():
    c = "Selenium"
    assert c.upper() == "SELENIUM"

@pytest.mark.A13
def test_3():
    assert True

@pytest.mark.test4
def test_4():
    assert False
