"""Contact list page"""

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from UI.Pages.base_page import BasePage
from logger import logger

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
        logger.info(f"Trying to find a button using locator: {add_button}.")
        btn = self.find_element(add_button)

        logger.info("Clicking add button.")
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

        logger.info(f"Trying to get row name using locator: {locator}.")
        el = self.find_element(locator)

        logger.info(f"Found row name: {el.text}.")
        return el.text

    def get_row_birthdate(self):
        """Get first row birthdate"""
        locator = (first_row[0], first_row[1] + "//td[3]")

        logger.info(f"Trying to get row birthdate using locator: {locator}.")
        el = self.find_element(locator)

        logger.info(f"Found row birthdate: {el.text}.")
        return el.text

    def get_row_email(self):
        """Get first row email"""
        locator = (first_row[0], first_row[1] + "//td[4]")

        logger.info(f"Trying to get row email using locator: {locator}.")
        el = self.find_element(locator)

        logger.info(f"Found row email: {el.text}.")
        return el.text

    def get_row_phone(self):
        """Get first row phone"""
        locator = (first_row[0], first_row[1] + "//td[5]")

        logger.info(f"Trying to get row phone using locator: {locator}.")
        el = self.find_element(locator)

        logger.info(f"Found row phone: {el.text}.")
        return el.text

    def get_row_address(self):
        """Get first row address"""
        locator = (first_row[0], first_row[1] + "//td[6]")

        logger.info(f"Trying to get row address using locator: {locator}.")
        el = self.find_element(locator)

        logger.info(f"Found row address: {el.text}.")
        return el.text

    def get_row_city(self):
        """Get first row city"""
        locator = (first_row[0], first_row[1] + "//td[7]")

        logger.info(f"Trying to get row city using locator: {locator}.")
        el = self.find_element(locator)

        logger.info(f"Found row city: {el.text}.")
        return el.text

    def get_row_country(self):
        """Get first row country"""
        locator = (first_row[0], first_row[1] + "//td[8]")

        logger.info(f"Trying to get row country using locator: {locator}.")
        el = self.find_element(locator)

        logger.info(f"Found row country: {el.text}.")
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
