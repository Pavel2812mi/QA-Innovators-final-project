"""Contact list page"""

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from UI.Pages.base_page import BasePage

add_button = (By.ID, "add-contact")
first_row = (By.XPATH, "//tr[@class='contactTableBodyRow'][1]")
logout_button = (By.ID, "logout")


class ContactListPage(BasePage):
    """Class Contact List Page"""
    def __init__(self, driver):
        """Initializes an instance of the example Class"""
        super().__init__(driver)

    def click_add_button(self):
        """Click add button"""
        btn = self.find_element(add_button)
        btn.click()

    def click_first_row(self):
        """Click first row"""
        row = self.find_element(first_row)
        row.click()

    def find_row(self):
        """Find row"""
        try:
            self.find_element(first_row)
            return True
        except NoSuchElementException:
            return False

    def get_row_name(self):
        """Get first row name"""
        locator = (first_row[0], first_row[1] + "//td[2]")
        el = self.find_element(locator)
        return el.text

    def get_row_birthdate(self):
        """Get first row birthdate"""
        locator = (first_row[0], first_row[1] + "//td[3]")
        el = self.find_element(locator)
        return el.text

    def get_row_email(self):
        """Get first row email"""
        locator = (first_row[0], first_row[1] + "//td[4]")
        el = self.find_element(locator)
        return el.text

    def get_row_phone(self):
        """Get first row phone"""
        locator = (first_row[0], first_row[1] + "//td[5]")
        el = self.find_element(locator)
        return el.text

    def get_row_address(self):
        """Get first row address"""
        locator = (first_row[0], first_row[1] + "//td[6]")
        el = self.find_element(locator)
        return el.text

    def get_row_city(self):
        """Get first row city"""
        locator = (first_row[0], first_row[1] + "//td[7]")
        el = self.find_element(locator)
        return el.text

    def get_row_country(self):
        """Get first row country"""
        locator = (first_row[0], first_row[1] + "//td[8]")
        el = self.find_element(locator)
        return el.text

    def get_all_row_data(self):
        """Get first row all data"""
        return [
            self.get_row_name(), self.get_row_birthdate(),
            self.get_row_email(), self.get_row_phone(), self.get_row_address(),
            self.get_row_city(), self.get_row_country()
            ]

    def click_logout_button(self):
        """Click logout button"""
        btn = self.find_element(logout_button)
        btn.click()
