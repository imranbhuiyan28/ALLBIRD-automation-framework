from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC




@given('I open the homepage on "{device}"')
def open_homepage(context, device):
    context.driver.get("https://www.allbirds.com/")

    if device == "desktop":
        context.driver.maximize_window()
        sleep(3)

    elif device == "tablet":
        context.driver.set_window_size(768, 1024)
        sleep(3)

    elif device == "mobile":
        context.driver.set_window_size(375, 667)
        sleep(3)

@then('the homepage layout should display correctly')
def verify_homepage_layout(context):
    width = context.driver.get_window_size()['width']
    if width > 1000:
        locator = (By.XPATH, "(//*[name()='path'][@id='Vector_2'])[2]")
    else:
        locator = (By.CSS_SELECTOR, '[title="Allbirds"]')

    logo = context.driver.wait.until(
        EC.visibility_of_element_located(locator)
    )

    assert logo.is_displayed(), "logo not visible"

    print("Successfully rendered the page")




@given('I measure the homepage load time')
def load_timeout(context):
    context.app.main_page.load_time()

@then('It should load in under 3 seconds')
def verify_load_time(context):
    context.app.main_page.verify_load_time()


