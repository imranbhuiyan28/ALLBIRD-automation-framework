Feature: Shopping Cart
  As a user
  I want to manage my cart
  So that I can proceed to checkout correctly


@smoke
  Scenario: Add product to cart
    Given open the homepage
    When I add the product to cart
    Then the cart should display the product
    Then Remove product from cart and Verify the cart should be empty

