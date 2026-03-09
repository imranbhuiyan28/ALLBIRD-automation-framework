from time import sleep, time
from selenium.webdriver.common.by import By
from behave import given, when, then
import time

from page.base_page import BasePage


class MainPage(BasePage):

    ALL_BIRD_LOGO = (By.XPATH, "(//*[name()='path'][@id='Vector_2'])[2]")

    def open(self):
        self.open_url('https://www.allbirds.com/')


    def page_title_contains(self,text):
        title = self.driver.title
        print(f"Page title is: {title}")
        assert text in title, f'Expected "{text}" in "{title}"'

    def verify_logo(self):
        logo = self.driver.find_element(*self.ALL_BIRD_LOGO)
        assert logo.is_displayed(), f'Expected "{logo.text}" to be displayed'
        print("Logo is displayed")



    def load_time(self):
        start = time.time()
        self.driver.get("https://www.allbirds.com/")
        end = time.time()
        self.load_time = end - start
        print(f"page load time: {self.load_time:2f}")



    def verify_load_time(self):
        assert self.load_time < 3, f"page is too slow and load time is {self.load_time:2f}"
        print("page load time within 3 seconds")
    