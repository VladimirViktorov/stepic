from pages.base_page import BasePage
from constant import LOGIN_PAGE_URL
from locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert login_url == LOGIN_PAGE_URL, f"Login url is not True. URL: '{login_url}'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Login form is not presented"
    
    def should_be_message_add_user(self):
        assert self.is_element_present(*LoginPageLocators.MESSAGE), "Messages is not presented"
    
    def register_new_user(self, email, password):
        registration_email = self.browser.find_element(*LoginPageLocators.registration_email)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", registration_email)
        registration_email.send_keys(email)
        registration_password1 = self.browser.find_element(*LoginPageLocators.registration_password1)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", registration_password1)
        registration_password1.send_keys(password)
        registration_password2 = self.browser.find_element(*LoginPageLocators.registration_password2)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", registration_password2)
        registration_password2.send_keys(password)
        button_registration = self.browser.find_element(*LoginPageLocators.button_registration)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", button_registration)
        button_registration.click()