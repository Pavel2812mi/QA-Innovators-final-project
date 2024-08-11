"""Authorization tests"""

import pytest
from UI.Pages.login_page import LoginPage
from UI.Test_data import test_data


@pytest.mark.login
def test_login_success(driver):
    """Test login successfully"""
    lp = LoginPage(driver)
    lp.complete_login(test_data.eml, test_data.psw)
    lp.wait_url(driver, test_data.url_contain1)
    assert test_data.url1 in driver.current_url
