from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from page.base_page import BasePage


class ProductPage(BasePage):
    SEARCH_BTN = (By.XPATH, "//li[@class='flex items-center justify-center']//a[@title='Search']")
    LOOKING_FOR = (By.CSS_SELECTOR, '[type="search"]')
    SEARCH_TEXT = (By.CSS_SELECTOR, '[class="text-light-charcoal mb-5 text-center text-sm opacity-0 md:mb-8"]')
    NO_RESULT = (By.CSS_SELECTOR, '[id="no-results-message"]')
    POPUP_CLOSE = (By.CSS_SELECTOR, "button, .close, .popup, .overlay")
    SHOP_MEN_BTN = (By.CSS_SELECTOR,'[class="shop-men btn btn-outline-black min-w-32"]')
    SIZE = (By.CSS_SELECTOR, '[aria-label="Select size 10"]')
    ADD_TO_CART = (By.CSS_SELECTOR,'[data-testid="pdp-atc-button"]')
    CART = (By.XPATH,"//button[@id='cart-drawer-checkout-button']")
    VERIFY_CART = (By.CSS_SELECTOR, '[class="_1tx8jg70 _1fragemsm _1tx8jg7i _1tx8jg7b _1fragemv5 _1tx8jg717 _1tx8jg71f _1tx8jg71h"]')
    MEN_BTN = (By.CSS_SELECTOR, "[data-testid= 'desktop-nav-trigger-men']")
    SHOP_ALL = (By.CSS_SELECTOR, "[data-testid= 'desktop-menu-column-individual-link-Shop All']")
    PRODUCT_IMG = (By.CSS_SELECTOR, '[class="absolute inset-0 overflow-hidden rounded-t-2xl"]')
    FILTER = (By.CSS_SELECTOR, '[class="flex items-center justify-center rounded-full border border-black p-1"]')
    SIZE_10 = (By.CSS_SELECTOR, '[for="Filter-filter.p.m.allbirds_v2.category_sizes-10"]')
    APPLY_FILTER = (By.XPATH, "//button[contains(text(),'Apply filters' )]")
    TOTAL_PRODUCT = (By.CSS_SELECTOR, '[class="text-sm text-gray-600"]')
    ALL_PRODUCT = (By.CSS_SELECTOR, '[class="absolute inset-0 overflow-hidden rounded-t-2xl"]')
    ALL_PRODUCT_NAME = (By.CSS_SELECTOR,'[class="mt-auto flex flex-col gap-2.5 justify-self-end p-2.5 sm:p-4')
    VERIFY_SIZE = (By.XPATH, "(//span[contains(text(),'10')])[2]")
    SORT_DROPDOWN = (By.ID, "SortBy")
    ALL_PRICE = (By.CSS_SELECTOR,  '[class="text-red')
    def search_for_product(self, product_name):
        self.click(*self.SEARCH_BTN)
        sleep(2)
        #search product name
        self.input_text(product_name,*self.LOOKING_FOR)
        sleep(5)

    def search_result_displayed(self,expected_text):
        self.verify_partial_text(expected_text,*self.SEARCH_TEXT)



    def no_results_displayed(self,message):
        self.click(*self.SEARCH_BTN)
        sleep(2)
        self.input_text(message,*self.LOOKING_FOR)
        sleep(5)

    def no_result_found(self,message):
        self.verify_partial_text(message,*self.NO_RESULT)

    def shop_for_men(self):
        self.click(*self.SHOP_MEN_BTN)


    def size(self):
        self.click(*self.SIZE)



    def add_to_cart(self):
        self.click(*self.ADD_TO_CART)
        sleep(4)
        self.click(*self.CART)
        sleep(5)

    def added_to_cart(self):

        title = self.find_element(*self.VERIFY_CART).text
        print(f"product name: {title} added to cart")
        assert title , f"No product added to cart"
        print("Successfully added to cart")


    def shop_all(self):
        self.wait.until(EC.element_to_be_clickable(self.MEN_BTN)).click()
        self.wait_for_element_clickable(*self.SHOP_ALL).click()
        sleep(5)

    def verify_image(self):
        image = self.driver.find_elements(*self.PRODUCT_IMG)
        print(f"Total image found: {len(image)}")
        for i, img in enumerate(image, start= 1):
            assert img.is_displayed(), f"Image is not visible : {i}"
        print("Successfully verified")

    def product_list(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.element_to_be_clickable(self.MEN_BTN)).click()
        wait.until(EC.element_to_be_clickable(self.SHOP_ALL)).click()
        sleep(3)

        all_product = self.driver.find_elements(*self.ALL_PRODUCT)
        print(f"Total product found: {len(all_product)}")



    def filter_by_size(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.FILTER)).click()
        self.click(*self.SIZE_10)
        wait.until(EC.element_to_be_clickable(self.APPLY_FILTER)).click()

        sleep(5)
        all_product = self.driver.find_elements(*self.ALL_PRODUCT)
        print(f"Now total product found after size 10: {len(all_product)}")
        product_names = self.driver.find_elements(*self.ALL_PRODUCT_NAME)
        for name in product_names:
            text = name.get_attribute("textContent").strip()
            product = text.split("$")[0]
            print(f"Product name: {product}")

    def verify_size(self, size):
        # Get all elements matching the locator
        size_elements = self.driver.find_elements(*self.VERIFY_SIZE)
        # Loop through each element and get its text
        for i in size_elements:
            text = i.text.strip()  # get text of this element
            print(f"Found size: {text}")
            assert text == size, f"Expected size {size} but found {text}"

        print(f"Successfully verified all displayed products have size {size}")


    def sort_by_price(self):
        dropdown = self.driver.find_element(*self.SORT_DROPDOWN)
        select = Select(dropdown)
        select.select_by_visible_text("Price, low to high") 
        sleep(10)

    def verify_sort(self):
        all_price_elements = self.driver.find_elements(*self.ALL_PRICE)
        all_price = []
        for i in all_price_elements:
            text = i.text.strip().replace("$", "").replace(",", "")
            if text:
                print(f"Found price: {text}")
                all_price.append(float(text))
        print(f"Total price found: ", all_price)
        if  all_price == sorted(all_price):
            print(f"Successfully verified all all price correctly")
        else:
            print(f"Sort failed")



