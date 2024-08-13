"""Tests"""
import time
import pytest
from UI.Pages.contact_list_page import ContactListPage
from UI.Pages.add_contact_page import AddContactPage
from UI.Pages.contact_details_page import ContactDetailsPage
from UI.Pages.edit_contact_page import EditContactPage
from UI.Test_data import test_data


@pytest.mark.add_contact
def test_add_contact(driver, login):
    """Test add contact successfully"""

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


def test_cancel_add_contact(driver, login):
    """Test cancel add contact successfully"""

    clp = ContactListPage(driver)
    clp.click_add_button()
    clp.wait_url(driver, test_data.url_contain2)
    assert test_data.url2 in driver.current_url

    acp = AddContactPage(driver)
    acp.click_cancel_button()
    assert test_data.url1 in driver.current_url


@pytest.mark.edit_contact
def test_edit_contact(driver, login):
    """Test edit contact successfully"""

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


def test_cancel_edit_contact(driver, login):
    """Test edit contact successfully"""

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
    ecp.click_cancel_button()
    ecp.wait_url(driver, test_data.url_contain3)
    assert test_data.url3 in driver.current_url

    cdp.click_delete_button()
    alert = driver.switch_to.alert
    alert.accept()
    cdp.wait_url(driver, test_data.url_contain1)
    clp = ContactListPage(driver)
    assert clp.find_row() is False


@pytest.mark.delete_contact
def test_delete_contact(driver, login):
    """Test delete contact successfully"""

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
