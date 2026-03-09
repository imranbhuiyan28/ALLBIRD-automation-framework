Feature: Product Search
  As a shopper
  I want to search for products
  So that I can find items to purchase

  Scenario: Search valid product
    Given open the homepage
    When when I search for "Wool Runner"
    Then search results for "Wool Runner" should be displayed


  Scenario: Search invalid product
    Given open the homepage
    When I search for "InvalidProductXYZ"
    Then I should see "Sorry, we couldn't find any results"


  

