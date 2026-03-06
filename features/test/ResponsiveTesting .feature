
@smoke
Feature: Responsive Design
  As a user
  I want the site to display correctly on all devices
  So that I can shop on mobile, tablet, and desktop

  Scenario Outline: Check homepage layout on different devices
    Given I open the homepage on "<device>"
    Then the homepage layout should display correctly

    Examples:
      | device  |
      | desktop |
      | tablet  |
      | mobile  |




   Scenario: Homepage loads within acceptable time
    Given I measure the homepage load time
    Then It should load in under 3 seconds