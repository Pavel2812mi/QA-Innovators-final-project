"""Tests"""
import time
import pytest

from UI.Pages.login_page import LoginPage
from UI.Pages.contact_list_page import ContactListPage
from UI.Pages.add_contact_page import AddContactPage
from UI.Pages.contact_details_page import ContactDetailsPage
from UI.Pages.edit_contact_page import EditContactPage
from UI.Test_data import test_data


@pytest.mark.add_contact
def test_add_contact(driver):
    """Test add contact successfully"""
    lp = LoginPage(driver)
    lp.complete_login(test_data.eml, test_data.psw)
    lp.wait_url(driver, test_data.url_contain1)
    assert test_data.url1 in driver.current_url

    clp = ContactListPage(driver)
    clp.click_add_button()
    clp.wait_url(driver, test_data.url_contain2)
    assert test_data.url2 in driver.current_url

    acp = AddContactPage(driver)
    acp.add_contact(test_data.fn, test_data.ln, test_data.bd,
                    test_data.eml1, test_data.pn, test_data.str1,
                    test_data.str2, test_data.ct, test_data.stpr,
                    test_data.pc, test_data.cntr)
    acp.wait_url(driver, test_data.url_contain1)
    clp.click_first_row()
    clp.wait_url(driver, test_data.url_contain3)
    assert test_data.url3 in driver.current_url
    cdp = ContactDetailsPage(driver)
    cdp.click_delete_button()
    alert = driver.switch_to.alert
    alert.accept()
    cdp.wait_url(driver, test_data.url_contain1)
    clp = ContactListPage(driver)
    assert clp.find_row() is False


@pytest.mark.edit_contact
def test_edit_contact(driver):
    """Test edit contact successfully"""
    lp = LoginPage(driver)
    lp.complete_login(test_data.eml, test_data.psw)
    lp.wait_url(driver, test_data.url_contain1)
    assert test_data.url1 in driver.current_url

    clp = ContactListPage(driver)
    clp.click_add_button()
    clp.wait_url(driver, test_data.url_contain2)
    assert test_data.url2 in driver.current_url

    acp = AddContactPage(driver)
    acp.add_contact(test_data.fn, test_data.ln, test_data.bd,
                    test_data.eml1, test_data.pn, test_data.str1,
                    test_data.str2, test_data.ct, test_data.stpr,
                    test_data.pc, test_data.cntr)
    acp.wait_url(driver, test_data.url_contain1)
    clp.click_first_row()
    clp.wait_url(driver, test_data.url_contain3)
    assert test_data.url3 in driver.current_url

    cdp = ContactDetailsPage(driver)
    cdp.click_edit_button()
    cdp.wait_url(driver, test_data.url_contain4)
    ecp = EditContactPage(driver)
    time.sleep(1)
    ecp.edit_contact(test_data.fn_1, test_data.ln_1, test_data.bd_1,
                     test_data.eml1_1, test_data.pn_1, test_data.str1_1,
                     test_data.str2_1, test_data.ct_1, test_data.stpr_1,
                     test_data.pc_1, test_data.cntr_1)
    ecp.wait_url(driver, test_data.url_contain3)
    time.sleep(1)
    assert cdp.get_first_name_text() == test_data.fn_1
    cdp = ContactDetailsPage(driver)
    cdp.click_delete_button()
    alert = driver.switch_to.alert
    alert.accept()
    cdp.wait_url(driver, test_data.url_contain1)
    clp = ContactListPage(driver)
    assert clp.find_row() is False


@pytest.mark.delete_contact
def test_delete_contact(driver):
    """Test delete contact successfully"""
    lp = LoginPage(driver)
    lp.complete_login(test_data.eml, test_data.psw)
    lp.wait_url(driver, test_data.url_contain1)
    assert test_data.url1 in driver.current_url

    clp = ContactListPage(driver)
    clp.click_add_button()
    clp.wait_url(driver, test_data.url_contain2)
    assert test_data.url2 in driver.current_url

    acp = AddContactPage(driver)
    acp.add_contact(test_data.fn, test_data.ln, test_data.bd,
                    test_data.eml1, test_data.pn, test_data.str1,
                    test_data.str2, test_data.ct, test_data.stpr,
                    test_data.pc, test_data.cntr)
    acp.wait_url(driver, test_data.url_contain1)
    clp.click_first_row()
    clp.wait_url(driver, test_data.url_contain3)
    assert test_data.url3 in driver.current_url
    cdp = ContactDetailsPage(driver)
    cdp.click_delete_button()
    alert = driver.switch_to.alert
    alert.accept()
    cdp.wait_url(driver, test_data.url_contain1)
    clp = ContactListPage(driver)
    assert clp.find_row() is False


@pytest.mark.view_contact
def test_view_contact(driver, created_contact):
    """Test view contact successfully"""
    clp = ContactListPage(driver)
    actual_result = clp.get_all_row_data()
    expected_result = [
        f"{test_data.fn} {test_data.ln}", test_data.bd, test_data.eml,
        test_data.pn, f"{test_data.str1} {test_data.str2}",
        f"{test_data.ct} {test_data.stpr} {test_data.pc}", test_data.cntr]
    assert actual_result == expected_result


@pytest.mark.view_contact
def test_view_empty_contact(driver, login_user):
    """Test view empty list contact successfully"""
    clp = ContactListPage(driver)
    assert clp.find_row() is False


@pytest.mark.add_contact
def test_add_contact_with_inv_data(driver, login_user):
    """Test add contact with invalid data unsuccessfully"""
    clp = ContactListPage(driver)
    clp.click_add_button()
    clp.wait_url(driver, test_data.url_contain2)
    assert test_data.url2 in driver.current_url

    acp = AddContactPage(driver)
    acp.add_contact(test_data.fn, test_data.ln, test_data.inv_bd,
                    test_data.inv_eml, test_data.inv_pn, test_data.str1,
                    test_data.str2, test_data.ct, test_data.stpr,
                    test_data.pc, test_data.cntr)
    assert (acp.get_error_message(test_data.error_message_add_new_contact)
            == test_data.error_message_add_new_contact)


@pytest.mark.add_contact
def test_add_contact_with_empty_data(driver, login_user):
    """Test add contact with empty data unsuccessfully"""
    clp = ContactListPage(driver)
    clp.click_add_button()
    clp.wait_url(driver, test_data.url_contain2)
    assert test_data.url2 in driver.current_url

    acp = AddContactPage(driver)
    acp.add_contact("", "", test_data.bd,
                    test_data.eml, test_data.pn, test_data.str1,
                    test_data.str2, test_data.ct, test_data.stpr,
                    test_data.pc, test_data.cntr)
    assert (acp.get_error_message(
            test_data.error_message_empty_add_new_contact) ==
            test_data.error_message_empty_add_new_contact)
