"""Contact details page"""

from selenium.webdriver.common.by import By
from UI.Pages.base_page import BasePage

edit_button = (By.ID, "edit-contact")
delete_button = (By.ID, "delete")
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


class ContactDetailsPage(BasePage):
    """Class Contact Details Page"""
    def __init__(self, driver):
        """Initializes an instance of the example Class"""
        super().__init__(driver)

    def click_edit_button(self):
        """Click edit button"""
        btn = self.find_element(edit_button)
        btn.click()

    def click_delete_button(self):
        """Click delete button"""
        btn = self.find_element(delete_button)
        btn.click()

    def get_first_name_text(self):
        """Get first name text"""
        el = self.find_element(first_name)
        return el.text

    def get_last_name_text(self):
        """Get last name text"""
        el = self.find_element(last_name)
        return el.text

    def get_birthdate_text(self):
        """Get birthdate text"""
        el = self.find_element(birthdate)
        return el.text

    def get_email_text(self):
        """Get email text"""
        el = self.find_element(email)
        return el.text

    def get_phone_text(self):
        """Get phone text"""
        el = self.find_element(phone)
        return el.text

    def get_address1_text(self):
        """Get address1 text"""
        el = self.find_element(street1)
        return el.text

    def get_address2_text(self):
        """Get address2 text"""
        el = self.find_element(street2)
        return el.text

    def get_city_text(self):
        """Get city text"""
        el = self.find_element(city)
        return el.text

    def get_state_province_text(self):
        """Get state province text"""
        el = self.find_element(state_province)
        return el.text

    def get_postal_code_text(self):
        """Get postal code text"""
        el = self.find_element(postal_code)
        return el.text

    def get_country_text(self):
        """Get country text"""
        el = self.find_element(country)
        return el.text

    def get_all_contact_details_data(self):
        """Get contact details all data"""
        return [
            self.get_first_name_text(), self.get_last_name_text(),
            self.get_birthdate_text(), self.get_email_text(),
            self.get_phone_text(), self.get_address1_text(),
            self.get_address2_text(), self.get_city_text(),
            self.get_state_province_text(), self.get_postal_code_text(),
            self.get_country_text()
            ]
