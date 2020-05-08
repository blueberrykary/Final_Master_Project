# story bored
* greet
  - utter_introduction
  - utter_introduction_r2
* choice_text{"choice":"text"}
  - action_choice_two
  - slot{"choice_two":"c_two"}
  - utter_ask_type_of_student
* bored
  - utter_bored
  - utter_thank_you_uprogram
  - utter_goodbye
  - action_restart

## story sad
* greet
  - utter_introduction
  - utter_introduction_r2
* choice_text{"choice":"text"}
  - action_choice_two
  - slot{"choice_two":"c_two"}
  - utter_ask_type_of_student
* sad
  - utter_sad
  - utter_thank_you_uprogram
  - utter_goodbye
  - action_restart

## story lazy
* greet
  - utter_introduction
  - utter_introduction_r2
* choice_text{"choice":"text"}
  - action_choice_two
  - slot{"choice_two":"c_two"}
  - utter_ask_type_of_student
* lazy
  - utter_lazy
  - utter_thank_you_uprogram
  - utter_goodbye
  - action_restart
