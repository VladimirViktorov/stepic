from pages.base_page import BasePage
from locators import BasketPageLocators

class BasketPage(BasePage):
    
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET), \
            "Product is presented, but should not be"
    
    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_EMPTY_BASKET), \
            "No text about empty basket"