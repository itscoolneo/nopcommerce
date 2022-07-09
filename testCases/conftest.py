import pytest
from selenium import webdriver
import configparser
@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    return driver
    # if browser == 'chrome':
    #     driver = webdriver.Chrome()
    #     print("Launching Chrome Browser")
    # elif browser == 'firefox':
    #     driver = webdriver.Firefox()
    #     print("Launching Firefox Browser")
    # else:
    #     driver = webdriver.Edge()
    # return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.option.browser("--browser")

################## PYTEST HTML REPORT ########################
def pytest_configure(config):
    config._metadata['Project Name']='nop Commerce'
    config._metadata['Module Name']='Customer'
    config._metadata['Tester Name'] = 'Dharmesh'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Plugins",None)

