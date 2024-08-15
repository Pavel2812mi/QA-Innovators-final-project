import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import uuid

from UI.Test_data import test_data


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


@pytest.fixture(scope="module")
def unique_email():
    """Fixture to generate a unique email"""
    return f"{uuid.uuid4()}@example.com"


@pytest.fixture(scope="module")
def existing_email():
    """Fixture to provide an existing email for testing"""
    return "john.doe112111@example.com"  # Этот email уже существует


@pytest.mark.signup
def test_successful_sign_up(driver, unique_email):
    """TC006: Check successful sign up for user with valid data"""
    driver.get("https://thinking-tester-contact-list.herokuapp.com/addUser")
    sp = SignUpPage(driver)
    sp.enter_first_name("John")
    sp.enter_last_name("Doe")
    sp.enter_email(unique_email)
    sp.enter_password("Password123!")
    sp.click_add_user()

    assert sp.is_signup_successful(), "User was not successfully signed up"


@pytest.mark.signup
def test_invalid_data_sign_up(driver):
    """TC007: Check sign up for user with invalid data"""
    driver.get("https://thinking-tester-contact-list.herokuapp.com/addUser")
    sp = SignUpPage(driver)
    sp.enter_first_name("John")
    sp.enter_last_name("Doe")
    sp.enter_email("invalid-email")
    sp.enter_password("w1")
    sp.click_add_user()

    error_message = sp.get_error_message()
    expected_error = (
        "User validation failed: email: Email is invalid, "
        "password: Path `password` (`w1`) is shorter than "
        "the minimum allowed length (7)."
    )
    assert error_message == expected_error, "No error message for invalid email"


@pytest.mark.signup
def test_existing_email_sign_up(driver, existing_email):
    """TC008: Check sign up for user with an existing email"""
    driver.get("https://thinking-tester-contact-list.herokuapp.com/addUser")
    sp = SignUpPage(driver)
    sp.enter_first_name("Jack")
    sp.enter_last_name("Vorobei")
    sp.enter_email(existing_email)  # Используем существующий email
    sp.enter_password("Password123!")
    sp.click_add_user()

    error_message = sp.get_error_message()
    assert error_message == "Email address is already in use", \
        "No error message for existing email"


@pytest.mark.signup
def test_empty_fields_sign_up(driver):
    """TC009: Check sign up for user with empty fields"""
    driver.get("https://thinking-tester-contact-list.herokuapp.com/addUser")
    sp = SignUpPage(driver)
    sp.click_add_user()

    error_message = sp.get_error_message()
    expected_error = (
        "User validation failed: firstName: Path `firstName` is required., "
        "lastName: Path `lastName` is required., email: Email is invalid, "
        "password: Path `password` is required."
    )
    assert error_message == expected_error, "No error message for empty fields"


@pytest.mark.signup
def test_cancel_sign_up(driver):
    """TC010: Check cancellation of sign-up process"""
    driver.get("https://thinking-tester-contact-list.herokuapp.com/addUser")
    sp = SignUpPage(driver)
    sp.enter_first_name("Temp")
    sp.enter_last_name("User")
    sp.enter_email("temp.user@example.com")
    sp.enter_password("TempPass123!")
    sp.click_cancel()

    assert driver.current_url == "https://thinking-tester-contact-list.herokuapp.com/login", \
        "User was not redirected to the home page after cancel"
