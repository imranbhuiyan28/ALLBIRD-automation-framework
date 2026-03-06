from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

SEARCH_BTN = (By.XPATH, "//li[@class='flex items-center justify-center']//a[@title='Search']")

@when('when I search for "{product_name}"')

def search_for_product(context, product_name):

    context.app.product_page.search_for_product(product_name)

@then('search results for "{product}" should be displayed')
def search_results_displayed(context, product):
    context.app.product_page.search_result_displayed(product)

@when('I search for "{message}"')
def invalid_results(context,message):
    context.app.product_page.no_results_displayed(message)


@then('I should see "{message}"')
def no_result(context, message):
    context.app.product_page.no_result_found(message)

@then("select for men")
def select_for_men(context):
    context.app.product_page.shop_for_men()

@when("I select size 10")
def select_size(context):
    context.app.product_page.size()

@when("I click Add to Cart")
def click_cart(context):
    context.app.product_page.add_to_cart()

@then("the product should be added to the cart")
def add_to_cart(context):
    context.app.product_page.added_to_cart()

@then('click shop all from header')
def select_all(context):
    context.app.product_page.shop_all()

@then('all product images should be visible')
def image_visible(context):
    context.app.product_page.verify_image()


@then('go to product list')
def go_to_product_list(context):
    context.app.product_page.product_list()

@when('I filter by size 10')
def filter_by_size(context):
    context.app.product_page.filter_by_size()

@then('all products displayed should have size "{size}"')
def verify_product_size(context, size):
    context.app.product_page.verify_size(size)

@when('I sort products by "Price: Low to High"')
def sort_products(context):
    context.app.product_page.sort_by_price()

@then('products should be sorted in ascending order by price')
def sort_products_by_price(context):
    context.app.product_page.verify_sort()