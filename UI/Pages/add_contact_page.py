"""Add contact page"""

from selenium.webdriver.common.by import By
from UI.Pages.base_page import BasePage
from logger import logger

first_name = (By.ID, "firstName")
last_name = (By.ID, "lastName")
birthdate = (By.ID, "birthdate")
email = (By.ID, "email")
phone = (By.ID, "phone")
street1 = (By.ID, "street1")
street2 = (By.ID, "street2")
city = (By.ID, "city")
state_province = (By.ID, "stateProvince")
postal_code = (By.ID, "postalCode")
country = (By.ID, "country")
submit_button = (By.ID, "submit")
cancel_button = (By.ID, "cancel")
error_message = (By.XPATH, "//span[@id='error']")


class AddContactPage(BasePage):
    """Class add contact page"""
    def __init__(self, driver):
        """Initializes an instance of the example Class"""
        super().__init__(driver)

    def enter_first_name(self, fn):
        """Enter first name"""
        logger.info(f"Trying to get first name using locator: {first_name}.")
        el_input = self.find_element(first_name)

        logger.info(f"Entering first name: {fn} into field: {el_input}.")
        el_input.send_keys(fn)

    def enter_last_name(self, ln):
        """Enter last name"""
        logger.info(f"Trying to get last name using locator: {last_name}.")
        el_input = self.find_element(last_name)

        logger.info(f"Entering last name: {ln} into field: {el_input}.")
        el_input.send_keys(ln)

    def enter_birthdate(self, bd):
        """Enter birthdate"""
        logger.info(f"Trying to get birthdate using locator: {birthdate}.")
        el_input = self.find_element(birthdate)

        logger.info(f"Entering birthdate: {bd} into field: {el_input}.")
        el_input.send_keys(bd)

    def enter_email(self, eml1):
        """Enter email"""
        logger.info(f"Trying to get email using locator: {email}.")
        el_input = self.find_element(email)

        logger.info(f"Entering email: {eml1} into field: {el_input}.")
        el_input.send_keys(eml1)

    def enter_phone(self, pn):
        """Enter phone"""
        logger.info(f"Trying to get phone using locator: {phone}.")
        el_input = self.find_element(phone)

        logger.info(f"Entering phone: {pn} into field: {el_input}.")
        el_input.send_keys(pn)

    def enter_street1(self, str1):
        """Enter street 1"""
        logger.info(f"Trying to get street1 using locator: {street1}.")
        el_input = self.find_element(street1)

        logger.info(f"Entering street1: {str1} into field: {el_input}.")
        el_input.send_keys(str1)

    def enter_street2(self, str2):
        """Enter street 2"""
        logger.info(f"Trying to get street2 using locator: {street2}.")
        el_input = self.find_element(street2)

        logger.info(f"Entering street2: {str2} into field: {el_input}.")
        el_input.send_keys(str2)

    def enter_city(self, ct):
        """Enter city"""
        logger.info(f"Trying to get city using locator: {city}.")
        el_input = self.find_element(city)

        logger.info(f"Entering city: {ct} into field: {el_input}.")
        el_input.send_keys(ct)

    def enter_state_province(self, stpr):
        """Enter state or province"""
        logger.info(f"Trying to get state province using "
                    f"locator: {state_province}.")
        el_input = self.find_element(state_province)

        logger.info(f"Entering state province: {stpr} into field: {el_input}.")
        el_input.send_keys(stpr)

    def enter_postal_code(self, pc):
        """Enter postal code"""
        logger.info(f"Trying to get postal code using locator: {postal_code}.")
        el_input = self.find_element(postal_code)

        logger.info(f"Entering postal code: {pc} into field: {el_input}.")
        el_input.send_keys(pc)

    def enter_country(self, cntr):
        """Enter country"""
        logger.info(f"Trying to get country using locator: {country}.")
        el_input = self.find_element(country)

        logger.info(f"Entering country: {cntr} into field: {el_input}.")
        el_input.send_keys(cntr)

    def click_submit_button(self):
        """Click submit button"""
        logger.info(f"Trying to get submit button using "
                    f"locator: {submit_button}.")
        btn = self.find_element(submit_button)

        logger.info(f"Click submit button.")
        btn.click()

    def click_cancel_button(self):
        """Click cancel button"""
        btn = self.find_element(cancel_button)
        btn.click()

    def add_contact(self, fn, ln, bd, eml1, pn, str1, str2,
                    ct, stpr, pc, cntr):
        """Add contact"""
        self.enter_first_name(fn)
        self.enter_last_name(ln)
        self.enter_birthdate(bd)
        self.enter_email(eml1)
        self.enter_phone(pn)
        self.enter_street1(str1)
        self.enter_street2(str2)
        self.enter_city(ct)
        self.enter_state_province(stpr)
        self.enter_postal_code(pc)
        self.enter_country(cntr)
        self.click_submit_button()

    def get_error_message(self, message):
        """Get error message"""
        if self.wait_value_in_element_appears(error_message, message):
            el = self.find_element_with_wait(error_message)
            return el.text
        return None
