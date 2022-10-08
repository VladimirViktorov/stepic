from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_TO_BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    MESSAGES = (By.CSS_SELECTOR, "#messages")
    VERIFICATION_NAME_BOOK = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    VERIFICATION_PRICE = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    NAME_BOOK = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    PRICE = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
