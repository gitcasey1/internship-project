# Created by kcfeb at 5/29/2024
Feature: Test scenario for secondary deals

  Scenario: User can filter the Secondary deals by Unit price range
    Given Open the main page
    When Click Sign in
    When Input caseyone1144@yahoo.com into email field
    When Input Newbeginning2024! into password field
    When Log in to the page
    When Click on Secondary option at the left side menu
    Then Verify the right page opens
    When Click Filters button at top center of page
    When Input Unit price (AED) from 1200000
    When Input Unit price (AED) to 2000000
    When Click Apply filter button
    Then Verify the price in all cards is inside the range (1200000 - 2000000)