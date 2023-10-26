Feature: Test Scenarios for Reely Page


  Scenario: The user clicks on “Connect Agency” button and sees the right number of UI elements
    Given Open Reely home page
    When Log into the page
    When Click on Connect Agency
    When Switch the new tab
    Then Verify there are 4 steps on the presentation page
    Then Verify Subscription plans button is clickable
