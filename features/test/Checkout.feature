Feature: Shopping Cart
  As a user
  I want to manage my cart
  So that I can proceed to checkout correctly
  @smoke

  Scenario: Add product to cart
    Given open the homepage
    When I add the product to cart
    Then the cart should display the product

  @smoke

  Scenario: Update product quantity
    Given open the homepage
    When I update the quantity to 3
    Then the cart total should reflect the quantity