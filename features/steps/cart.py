from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep




@when('I add the product to cart')
def adding_to_cart(context):
    context.app.cart_page.adding_cart()


@then('the cart should display the product')
def displaying_product(context):
    context.app.cart_page.checkout()


@then('Remove product from cart and Verify the cart should be empty')
def removing_product(context):
    context.app.cart_page.remove_product()


@when ('I update the quantity to {qty}')
def updating_quantity(context,qty):
    context.app.cart_page.update_quantity(int(3))


@then('the cart total should reflect the quantity')
def cart_total(context):
    context.app.cart_page.total_cart_price()