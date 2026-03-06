from page.base_page import BasePage
from page.main_page import MainPage
from page.footer_page import FooterPage
from page.product_page import ProductPage
from page.cart_page import CartPage



class Application:
    def __init__(self,driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.main_page = MainPage(driver)
        self.footer_page = FooterPage(driver)
        self.product_page = ProductPage(driver)
        self.cart_page = CartPage(driver)