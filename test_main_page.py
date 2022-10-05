from pages.main_page import MainPage
from constant import MAIN_PAGE_URL


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, MAIN_PAGE_URL)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, MAIN_PAGE_URL)
    page.open()
    page.should_be_login_link()

