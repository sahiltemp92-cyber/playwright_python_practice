Feature: Order Transaction
    Tests related to order transations

    Scenario Outline: Verify order success message is shown in details page
        Given Place the item order with <username> and <password>
        And the user is on landing page
        When I login to portal with <username> and <password>
        And Navigate to orders page
        And Select the order id
        Then order message is successfully displayed

        Examples:
        | username                      | password    | order id                |
        | sahil.khenat.career@gmail.com | Rahul@12345 | 6a99d06ae7cd69710fbd5341 |