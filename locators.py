from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    registration_email = (By.CSS_SELECTOR, "#id_registration-email")
    registration_password1 = (By.CSS_SELECTOR, "#id_registration-password1")
    registration_password2 = (By.CSS_SELECTOR, "#id_registration-password2")
    button_registration = (By.XPATH, "//*[@id='register_form']/button")
    MESSAGE = (By.CSS_SELECTOR, "#messages")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class ProductPageLocators():
    ADD_TO_BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    MESSAGE = (By.CSS_SELECTOR, "#messages")
    VERIFICATION_NAME_BOOK = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    VERIFICATION_PRICE = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    NAME_BOOK = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    PRICE = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")

class BasketPageLocators():
    BASKET_FORMSET = (By.CSS_SELECTOR, "#basket_formset")
    TEXT_EMPTY_BASKET = (By.XPATH, "//*[@id='content_inner']/p")