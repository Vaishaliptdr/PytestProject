Feature: Order transaction
  Tests related to order transaction
  Scenario Outline: To verify order success messages shown up in details page
    Given place the item order with <username> and <password>
    And the user is on landing page
    When User will login to portal with <username> and <password>
    And navigate to orders page
    And select the order id
    Then order message will successfully displayed
    Examples:
      | username                 | password     |
      | vaishalidusane@gmail.com | Learning@123 |
      | anshika@gmail.com        | Iamking@000  |