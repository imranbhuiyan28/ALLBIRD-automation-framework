from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.base_page import BasePage

class CartPage(BasePage):

    ADD_CART = (By.CSS_SELECTOR, '[class="font-sans text-xs font-medium tracking-wider uppercase"]')
    SHOE_SIZE = (By.XPATH, "(//span[contains(text(),'10')])[7]")
    CHECK_OUT = (By.CSS_SELECTOR, '[id="cart-drawer-checkout-button"]')
    PRODUCT_DISPLAY = (By.CSS_SELECTOR, '[class="_1tx8jg70 _1fragemsm _1tx8jg7i _1tx8jg7b _1fragemv5 _1tx8jg717 _1tx8jg71f _1tx8jg71h"]')
    HOME_PAGE = (By.CSS_SELECTOR, '[class="s2kwpi1 s2kwpi0 _1fragemsm _1fragemyw _1fragemz2 _1fragemyq s2kwpi3 s2kwpi6 s2kwpi9 s2kwpi7 _1fragem32 _1fragemvq"')
    CAR_BUTTON = (By.XPATH, "(//*[name()='svg'][@class='size-6'])[8]")
    REMOVE_ITEM = (By.CSS_SELECTOR, '[title="Remove item"]')
    CART_EMPTY = (By.CSS_SELECTOR, '[class="mb-10 px-5 text-center text-xl md:px-10"]')
    Update_QUANTITY = (By.CSS_SELECTOR, '[aria-label="Increase quantity"]')
    CART_PRICE = (By.CSS_SELECTOR, '[class="block text-sm font-medium"]' )
    TOTAL_CART_PRICE = (By.XPATH, "//p[contains(text(),'$345')]")
    def adding_cart(self):
        #finding the add to cart
        BTN = self.driver.find_elements(*self.ADD_CART)
        element = BTN[3]

        #middle of the page where button placed
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
        print(f"totall product: {len(BTN)}")
        element.click()
        shoe_size = self.driver.find_element(*self.SHOE_SIZE)
        shoe_size.click()
        sleep(2)
        self.click(*self.CHECK_OUT)
        sleep(5)



    def checkout(self):
        product = self.driver.find_element(*self.PRODUCT_DISPLAY).text
        print(product)
        assert product, "No product found in cart!"
        print(f"Products in cart: {product} and successfully Verified!)")


    def remove_product(self):
        self.click(*self.HOME_PAGE)
        sleep(2)
        self.click(*self.CAR_BUTTON)
        sleep(2)
        self.click(*self.REMOVE_ITEM)
        sleep(10)
        actual_text = self.driver.find_element(*self.CART_EMPTY).text
        print(actual_text)
        expected = 'Your cart is empty. Start shopping!'
        assert expected in actual_text, f"removing product from cart failed"
        print(f"Successfully removed product from cart")



    def update_quantity(self,qty):
        wait = WebDriverWait(self.driver, 15)
        BTN = self.driver.find_elements(*self.ADD_CART)
        element = BTN[3]
        element.click()
        shoe_size = self.driver.find_element(*self.SHOE_SIZE)
        shoe_size.click()
        sleep(2)
        product_text= self.driver.find_element(*self.CART_PRICE).text
        print(f"Shoe price: {product_text}")
        #storing the price for global use
        self.product_price = float(product_text.replace("$", ""))

        # ✅ store quantity
        self.qty = qty


        for _ in range(qty - 1):
            increase_BTN = wait.until(
                EC.element_to_be_clickable(self.Update_QUANTITY)
            )

            increase_BTN.click()
            sleep(5)

    def total_cart_price(self):
        total_text = self.driver.find_element(*self.TOTAL_CART_PRICE).text
        print(f"shoe total price: {total_text}")
        cart_total = float(total_text.replace("$", ""))
        expected_total = self.product_price * self.qty
        print("Expected:", expected_total)
        print("Actual:", cart_total)
        assert cart_total == expected_total, f"wrong total price"
        print(f"Successfully verified!")

