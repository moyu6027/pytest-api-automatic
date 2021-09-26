# Aries Automation based on Serenity BDD Screenplay Pattern

Experienced automated testers use layers of abstraction to separate the intent of the test (what you are trying to achieve) from the implementation details (how you achieve it). By separating the what from the how, the intent from the implementation, layers of abstraction help make tests easier to understand and to maintain. Indeed, well defined layers of abstraction are perhaps the single most important factor in writing high quality automated tests.

## How to use?

1. run `mvn clean verify`
2. see the report on target/site/serenity/index.html

### System properties

- hcc.test.type, set to `API` for API test, set to `Web` for web ui test, default to API test.
- cucumber.options, set the command options of the cucumber cli

below is an example to set the system properties before running the test  
`mvn "-Dcucumber.options=--tags '@issue:RCN-3890 and @API'" "-Dhcc.test.type=API" clean verify`

## The architecture

From top to down levels:
- capabilities (what to do)
- features (how to do)
- scenarios / examples
- step in natural language
- step definitions
- Actor has Ability / perform Tasks / ask Questions (the business layer)
- client / repository / actor perform actions (supported by appium & rest-assured) (the technical layer)
