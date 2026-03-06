from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

OUR_STORY = (By.XPATH, "//a[contains(text(), 'Our Stores')]")
ALL_BIRD_LOGO = (By.XPATH, "(//*[name()='path'][@id='Vector_2'])[2]")
FOOTER_LINKS = (By.CSS_SELECTOR, 'footer a.text-xs.hover\\:underline')

@given("open the homepage")
def open_website(context):
    context.app.main_page.open()

@then("the page title should contain Allbirds")
def page_title_contains(context):
    context.app.main_page.page_title_contains("Allbirds")


@then ("Verify there is logo")
def verify_logo(context):
    context.app.main_page.verify_logo()


@then ("I click on our story button")
def click_shop(context):

    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    context.driver.implicitly_wait(2)
    context.app.base_page.click(*OUR_STORY)
    sleep(2)
@when("I click the Allbirds logo, should be redirected to the homepage")
def click_logo(context):
    context.app.base_page.click(*ALL_BIRD_LOGO)
    sleep(5)



@then("all footer links should navigate to the correct page")
def all_footer_links(context):
    context.app.footer_page.verify_footer()


@then("all social media icons should open correct URLs")
def all_social_media_icons(context):
    context.app.footer_page.verify_social_media_icons()


