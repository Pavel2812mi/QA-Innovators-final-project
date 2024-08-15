import pytest
from UI.Pages.signUppage import SignUpPage


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
    assert error_message == expected_error, ("No error message "
                                             "for invalid email")


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

    assert driver.current_url == ("https://thinking-tester-cont"
                                  "act-list.herokuapp.com/login"), \
        "User was not redirected to the home page after cancel"
