Feature: Homepage
  As a user
  I want to navigate and validate the homepage
  So that the main sections and links work correctly

  Scenario: Verify homepage loads successfully
    Given  open the homepage
    Then the page title should contain Allbirds

@smoke
  Scenario: Verify logo redirects to homepage
    Given open the homepage
    Then  Verify there is logo
    Then I click on our story button
    When I click the Allbirds logo, should be redirected to the homepage


@smoke
  Scenario: Verify footer links
    Given open the homepage
    Then all footer links should navigate to the correct page
@smoke
  Scenario: Verify social media links
    Given open the homepage
    Then all social media icons should open correct URLs