from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class SignUpPage:
    """Class for interacting with the sign-up page"""

    def __init__(self, driver):
        """Initializes an instance of the SignUpPage"""
        self.driver = driver
        self.first_name = (By.ID, "firstName")
        self.last_name = (By.ID, "lastName")
        self.email = (By.ID, "email")
        self.password = (By.ID, "password")
        self.add_user_button = (By.ID, "submit")
        self.cancel_button = (By.ID, "cancel")
        self.error_element = (By.ID, "error")

    def enter_first_name(self, name):
        """Enter first name"""
        self.driver.find_element(*self.first_name).send_keys(name)

    def enter_last_name(self, name):
        """Enter last name"""
        self.driver.find_element(*self.last_name).send_keys(name)

    def enter_email(self, email):
        """Enter email"""
        self.driver.find_element(*self.email).send_keys(email)

    def enter_password(self, password):
        """Enter password"""
        self.driver.find_element(*self.password).send_keys(password)

    def click_add_user(self):
        """Click on the add user button"""
        self.driver.find_element(*self.add_user_button).click()

    def click_cancel(self):
        """Click on the cancel button"""
        self.driver.find_element(*self.cancel_button).click()

    def get_error_message(self):
        """Retrieve the error message displayed on the sign-up page"""
        try:
            error_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.error_element)
            )
            return error_element.text
        except NoSuchElementException:
            return ""

    def is_signup_successful(self):
        """Check if signup was successful by looking for
        a specific element on the homepage"""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("contactList")
            )
            return True
        except NoSuchElementException:
            return False
