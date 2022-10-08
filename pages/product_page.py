from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators import ProductPageLocators

class ProductPage(BasePage): 
    
    def add_product_to_basket(self):
        add_to_basket_form = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_FORM)
        add_to_basket_form.click()
        BasePage.solve_quiz_and_get_code(self)
    
    def should_be_product_adding_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGES), "Messages is not presented"
    
    def name_comparison(self):
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        verification_name_book = self.browser.find_element(*ProductPageLocators.VERIFICATION_NAME_BOOK).text
        assert name_book == verification_name_book, f"Names don't match. Name book: '{name_book}'. Verification name book: '{verification_name_book}'"
    
    def price_comparison(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        verification_price = self.browser.find_element(*ProductPageLocators.VERIFICATION_PRICE).text
        assert price == verification_price, f"Price don't match. Price: '{price}'. Verification price: '{verification_price}'"