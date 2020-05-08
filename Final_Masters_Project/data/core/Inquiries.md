<!--
## Karen Salinas
## CSC 590
## Story for inquiries
-->


## Slots of payloads
* greet
  - utter_introduction
  - utter_introduction_r2
* choice_payloads{"choice":"payloads"}
  - action_choice_one
  - slot{"choice_one":"c_one"}
  <!-- - utter_information
* help_inq -->
  - utter_menu

## Inquiry Student Makes with more details
* greet
  - utter_introduction
  - utter_introduction_r2
* choice_payloads{"choice":"payloads"}
  - action_choice_one
  - slot{"choice_one":"c_one"}
  <!-- - utter_information
* help_inq -->
  - utter_menu
* begin_lead
  - utter_lead_q1
  - lead_form_p1
  - form{"name": "lead_form_p1"}
  - form{"name": null}
* accept
  - lead_form_p2
  - form{"name": "lead_form_p2"}
  - form{"name": null}
  - lead_form_p3
  - form{"name": "lead_form_p3"}
  - form{"name": null}
  - utter_lead_q3
  - utter_lead_q4
  - utter_lead_q5
  - utter_thank_you_uprogram
* goodbye
  - utter_goodbye
  - action_restart

## Inquiry Student Makes With Less Details
* greet
  - utter_introduction
  - utter_introduction_r2
* choice_payloads{"choice":"payloads"}
  - action_choice_one
  - slot{"choice_one":"c_one"}
  <!-- - utter_information
* help_inq -->
  - utter_menu
* begin_lead
    - utter_lead_q1
    - lead_form_p1
    - form{"name": "lead_form_p1"}
    - form{"name": null}
* reject
    - lead_form_p3
    - form{"name": "lead_form_p3"}
    - form{"name": null}
    - utter_lead_q3
    - utter_lead_q4
    - utter_lead_q5
    - utter_thank_you_uprogram
* goodbye
  - utter_goodbye
  - action_restart
