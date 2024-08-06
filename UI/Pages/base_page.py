"""Base page"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Class Base Page"""
    def __init__(self, driver):
        """Initializes an instance of the example Class"""
        self.driver = driver

    def open(self, url):
        """Get driver url method"""
        self.driver.get(url)

    def find_element(self, selector):
        """Find element method"""
        return self.driver.find_element(*selector)

    def wait_url(self, driver, data):
        """Wait until the URL contains the specified fragment"""
        WebDriverWait(driver, 10).until(EC.url_contains(data))
