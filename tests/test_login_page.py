import requests as requests
import time
import db_queries
from settings import VALID_EMAIL_SELLER

from pages.locators import MainPageLocators, LoginPageLocators

from pages.login_page import LoginPage

link = 'https://dev.abra-market.com/login'


def test_login(browser):
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.go_to_button_submit()
    time.sleep(2)

    response = requests.get('https://dev.abra-market.com/')
    assert response.status_code == 200, f"{response.status_code} is not our expectation"
    profile_btn = browser.find_element(*MainPageLocators.PROFILE_BTN)
    assert f"'{profile_btn}' is present"
    assert len(db_queries.get_user_by_email(VALID_EMAIL_SELLER)) > 0


def test_login_with_invalid_password(browser):
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_invalid_password()
    error_invalid_password = browser.find_element(*LoginPageLocators.INVALID_PASSWORD)
    assert error_invalid_password.text == 'Invalid password', f" '{error_invalid_password.text}' is not expected text of error"
    assert browser.find_element(*LoginPageLocators.LOGIN_BTN).get_attribute("disabled") is not None


def test_login_with_empty_data(browser):
    page = LoginPage(browser, link)
    page.open()
    page.go_to_empty_login_data()
    error_email_is_required = browser.find_element(*LoginPageLocators.EMAIL_IS_REQUIRED)
    assert error_email_is_required.text == 'Email is required', f" '{error_email_is_required.text}' is not expected text of error"
    error_password_is_required = browser.find_element(*LoginPageLocators.PASSWORD_IS_REQUIRED)
    assert error_password_is_required.text == 'Password is required', f" '{error_password_is_required.text}' is not expected text of error"
    assert browser.find_element(*LoginPageLocators.LOGIN_BTN).get_attribute("disabled") is not None


def test_login_visible_password(browser):
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    password_visibility = browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
    assert password_visibility.get_attribute("type") == "password"
    page.go_to_password_visibility()
    time.sleep(2)
    assert password_visibility.get_attribute("type") == "text"
