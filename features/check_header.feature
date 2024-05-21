# This is a simple test just to Check if we can open the Elucidat page
Feature: Check Header

  Scenario: Verify the header text on the page
    Given I open the Elucidat webpage
    Then the header should be "FINDING THE TRUTH"
