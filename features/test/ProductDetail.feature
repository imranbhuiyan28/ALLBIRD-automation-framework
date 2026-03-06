@smoke
Feature: Product Detail Page
  As a shopper
  I want to view product details
  So that I can make purchase decisions

  Scenario: Add product to cart
    Given open the homepage
    Then  select for men
    When I select size 10
    And I click Add to Cart
    Then the product should be added to the cart
    

  Scenario: Verify product images load
    Given open the homepage
    Then click shop all from header
    And all product images should be visible