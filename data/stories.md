## go back to search for student 1
* go_back
  - utter_greet
  <!-- - utter_next -->
<!-- * go_back{"back":"go"}
  - action_goback
  - slot{"go":"go"} -->

## search for student 2
* greet
  - utter_greet
* search_student_two{"stud_two":"future student"}
  - action_search_student_two
  - slot{"student_num_two":"Future Student"}

# search for Instructor
* greet
  - utter_greet
* search_instruct{"instruct":"teacher"}
  - action_search_instruct
  - slot{"instruct_one": "teacher"}

* mood_great
  - utter_happy
<!--
* greet
  - fetch_profile
  - slots{"user_type": "current student"}
  - utter_greet -->


## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
