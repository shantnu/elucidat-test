# Check the score is a number, and nothing else
Feature: Check score is number
Scenario: Verify the score is a number
    Given I open the Elucidat webpage
    And Go to the score page
    Then the score should only be a number