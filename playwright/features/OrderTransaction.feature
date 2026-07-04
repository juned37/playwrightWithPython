Feature: Order Transaction
    Test Related to Order Transaction
    
    Scenario Outline: Verify Order Details Page
        Given Place order with <username> and <password>
        And Verify user is on landing page
        When Login with <username> and <password>
        And Navigate to Order page
        Then select orderid
        Examples:
            | username                  | password     |
            | 3737junedbagban@gmail.com | Juned@123    |