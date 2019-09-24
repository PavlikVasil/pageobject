from .base_page import BasePage
import time
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
from .product_page import PageObject

class LoginPage(PageObject, LoginPageLocators):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self, browser):
        assert browser.current_url, "is not found"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_FORM), "Is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*MainPageLocators.REG_FORM), "Is not presented"
        assert True

        
        
    def  register_new_user(self,email = str(time.time()) + "@fakemail.org", password = 'Uptowner24'):
        email = str(time.time()) + "@fakemail.org"
        password = 'Uptowner24'
        mail=self.browser.find_element(*LoginPageLocators.MAIL).send_keys(email)
        pswrd=self.browser.find_element(*LoginPageLocators.PSWRD).send_keys(password)
        pswrd2=self.browser.find_element(*LoginPageLocators.PSWRD2).send_keys(password)
        reg=self.browser.find_element(*LoginPageLocators.REG).click()
