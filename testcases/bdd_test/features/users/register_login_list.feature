@Scenario @Users @API
  Feature: As a new-monitor user, I want to be login for access login page
    so I must register and login, and I should can get Current User's Info

    Background: Sean have been authorized
      Given Sean have been authorized

      Rule: dddd
    Scenario Outline: Sean access login page and get personal info success
      When Access user "<path>" API
      Then The status code should be "<status_code>"
      And The response should correct format
      Examples:
        | path   | status_code |
        | /login | 200         |



    Scenario Outline: Sean want get personal info but error behavior make it failed
      Given Sean Access <path> API
      When Sean implement <type> behavior
      Then The status code should be <status_code>
      And Response should be '<message>' and <code>
      Examples:
        | path | type | status_code | message | code |
        | /user/getCurrentUser | ERROR_METHOD | 200 | internal error | 400003 |
        | /user/getCurrentUser | ERROR_COOKIE | 401 | User not login. | 111111 |