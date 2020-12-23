Feature: mycroft-FarmSkill

  Scenario: Talk to me baby
    Given an english speaking user
     When the user says "talk to me baby"
     Then "mycroft-FarmSkill" should reply with dialog from "how.is.my.farm.doing.dialog"

  Scenario: How is my farm doing
    Given an english speaking user
     When the user says "How is my farm doing"
     Then "mycroft-FarmSkill" should reply with dialog from "how.is.my.farm.doing.dialog"

  Scenario: What to do today
    Given an english speaking user
     When the user says "What to do today"
     Then "mycroft-FarmSkill" should reply with dialog from "how.is.my.farm.doing.dialog"