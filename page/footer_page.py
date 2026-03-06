from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page.base_page import BasePage
FOOTER_LINKS = (By.CSS_SELECTOR, 'footer a.text-xs.hover\\:underline')
SOCIAL_LINKS = (By.CSS_SELECTOR, ".social-icon")
INSTAGRAM_LINKS = (By.CSS_SELECTOR, '[aria-label="Instagram"]')


class FooterPage(BasePage):
    def verify_footer(self):
        print("Running footer verification...")

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)

        footer_links = self.driver.find_elements(*FOOTER_LINKS)

        print(f"Found {len(footer_links)} footer links")

        assert len(footer_links) > 0, "No footer links found!"

    def verify_social_media_icons(self):
        # Scroll to bottom
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #store current window

        parent_windows = self.driver.current_window_handle
        print(f"Curent windows: {parent_windows}")

        # get all the social media
        social_media_links = self.wait.until(EC.presence_of_all_elements_located(SOCIAL_LINKS))
        print(f"Found {len(social_media_links)} social media links")

        for idx, link in enumerate(social_media_links, start=1):
            print(f"Checking {idx}th social media link...")
            link.click()
            # Wait for new tab to open
            self.wait.until(lambda driver: len(driver.window_handles) > 1)
            all_windows = self.driver.window_handles



            #switch to new tab
            for window in all_windows:
                if window != parent_windows:
                    self.driver.switch_to.window(window)
                    break
            print(f"Switched to new window: {self.driver.current_window_handle}")
            print(f"New page URL: {self.driver.current_url}")
            new_url = self.driver.current_url

            assert new_url != "", "social media link not found!"

            #close all tab
            self.driver.close()

            self.driver.switch_to.window(parent_windows)

        print("All social media links opened successfully!")












