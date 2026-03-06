@smoke
Feature: Product Listing Page
  As a user
  I want to filter and sort products
  So that I can find what I want easily

  Scenario: Filter by size
    Given open the homepage
    Then go to product list
    When I filter by size 10
    Then all products displayed should have size "10"

  Scenario: Sort products by price low to high
    Given open the homepage
    Then go to product list
    When I sort products by "Price: Low to High"
    Then products should be sorted in ascending order by price