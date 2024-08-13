"""Conftest module"""
import pytest
from selenium import webdriver
from UI.Test_data import test_data
from UI.Pages.login_page import LoginPage


@pytest.fixture
def driver():
    """Fixture for initializing and quitting a Chrome WebDriver instance"""
    chrome = webdriver.Chrome()
    chrome.implicitly_wait(5)
    chrome.get(test_data.url)
    yield chrome
    chrome.quit()


@pytest.fixture
def login(driver):
    """Fixture for initializing and quitting a Chrome WebDriver instance"""
    lp = LoginPage(driver)
    lp.complete_login(test_data.eml, test_data.psw)
    lp.wait_url(driver, test_data.url_contain1)
    assert test_data.url1 in driver.current_url
