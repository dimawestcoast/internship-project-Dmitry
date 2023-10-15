Feature: Test Scenarios for Reely Page

#  Scenario: User can search for a product
#    Given Open Google page
#    When Input Car into search field
#    And Click on search icon
#    Then Product results for Car are shown

  Scenario: The user clicks on “Connect Agency” button and sees the right number of UI elements
    Given Open Reely home page
    When Log into the page
    When Click on Connect Agency
    When Switch the new tab
    Then Verify there are 4 steps in the description.
    Then Verify Subscription plans button is clickable
