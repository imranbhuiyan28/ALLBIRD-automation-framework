from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from support.logger import logger
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, url):
        self.driver.get(url)
        logger.info(f"Opening url: {url}")

    def click(self, *locator):
        logger.info(f"Clicking element: {locator}")
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        logger.info(f"Finding element: {locator}")
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        logger.info(f"Finding elements: {locator}")
        return self.driver.find_elements(*locator)

    def input_text(self,  text,  *locator):
        self.driver.find_element(*locator).send_keys(text)

    def wait_for_element_visible(self, *locator):
        return self.wait.until(EC.visibility_of_element_located(locator),
                               message=f"element by {locator} not visible"
                               )

    def wait_for_element_invisible(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator),
                        message=f"element by {locator} not invisible"
                        )

    def wait_for_element_clickable(self, *locator):
        return self.wait.until(EC.element_to_be_clickable(locator),
                               message=f"element by {locator} not clickable"
                               )

    def wait_and_click(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator),
                        message=f"element by {locator} not clickable"
                        ).click()


    def hover_element(self, *locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()


    def get_current_window_handle(self):
        return self.driver.current_window_handle


    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print(f"all_windows: {all_windows}")
        self.driver.switch_to.window(all_windows[1])
        print("current windows: ", self.driver.current_window_handle)

    def switch_to_windows_by_id(self, window_id):
        self.driver.switch_to.window(window_id)
        print('Current window ', self.driver.current_window_handle)

    #loading time
    def measure_load_time(self, url, threshold=3):
        start = time.time()
        self.driver.get(url)
        end = time.time()
        load_time = end - start
        print(f"Loading time: {load_time:.2f} seconds")
        logger.info(f"Page load time: {load_time:.2f} seconds")
        assert load_time < threshold, f"Homepage loaded in {load_time:.2f} s, which exceeds the {threshold}s limit"
        return load_time




    # Verifying section

    def verify_partial_text(self,expected_text, *locator):
        actual_text = self.find_element(*locator).text
        print(f"actual text: {actual_text}")
        assert expected_text in actual_text, f"expected {expected_text} not in {actual_text}"
        print(f"successfully verified")

    def verify_text(self,expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, f"expected {expected_text} not in {actual_text}"
        print(f"Text is verified")

    def verify_partial_url(self, expected_url, *locator):
        actual = self.driver.current_url
        print(f"current url is {expected_url}")
        assert expected_url in actual, f"expected {expected_url} not in {actual}"
        print("test passed")