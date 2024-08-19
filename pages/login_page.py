from settings import VALID_EMAIL_SELLER, VALID_PASSWORD, INVALID_PASSWORD

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def go_to_login(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys(VALID_EMAIL_SELLER)

    def go_to_password(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys(VALID_PASSWORD)

    def go_to_invalid_password(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys(INVALID_PASSWORD)
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).click()

    def go_to_button_submit(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_BTN).submit()

    def go_to_empty_login_data(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys('')
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys('')
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).click()

    def go_to_password_visibility(self):
        self.browser.find_element(*LoginPageLocators.PASSWORD_VISIBILITY).click()
