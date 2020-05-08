<!--
## Karen Salinas
## CSC 590
## Story for Campus Tour, Campus Map, and Campus Employment (Small Stories)
-->

## Story to view financial aid, enrollment, and computer science 500 then ending the program mixed up
* greet
  - utter_introduction
  - utter_introduction_r2
* choice_text{"choice":"text"}
  - action_choice_two
  - slot{"choice_two":"c_two"}
  - utter_ask_type_of_student
* student_type_two{"student_recurr":"ongoing student", "student_recurr": "freshman", "student_recurr":"sophmore", "student_recurr":"junior", "student_recurr":"senior", "student_recurr": "master's student", "student_recurr": "first year  student", "student_recurr":"second year student", "student_recurr" : "third year student", "student_recurr": "fourth year student", "student_recurr": "fifth year student", "student_recurr":"graduate student", "student_recurr": "undergraduate student", "student_recurr": "international student", "student_recurr":"recurring student", "student_recurr":"continuing student", "student_recurr": "recurring undergraduate student", "student_recurr": "recurring graduate student", "student_recurr": "ongoing undergraduate student", "student_recurr":"ongoing graduate student"}
  - action_searchrecurringstudent
  - slot{"rinfo":"rstudent"}
  - utter_current_student
* good_thanks
  - utter_great
* yes_ido
  - utter_ask1
* on_campus{"campus_CSUDH":"campus"}
  - action_campus_info
  - slot{"campus_information":"campus_info"}
  - utter_campus_info
* on_campus_tour{"campus_tour_CSUDH":"campus tour"}
  - action_oncampus_tour
  - slot{"on_campus_tour_info":"campus_tour_info"}
  - utter_thank_you_uprogram
* goodbye
  - utter_goodbye
  - action_restart


## Story to view financial aid, enrollment, and computer science 500 then ending the program mixed up
* greet
  - utter_introduction
  - utter_introduction_r2
* choice_text{"choice":"text"}
  - action_choice_two
  - slot{"choice_two":"c_two"}
  - utter_ask_type_of_student
* student_type_two{"student_recurr":"ongoing student", "student_recurr": "freshman", "student_recurr":"sophmore", "student_recurr":"junior", "student_recurr":"senior", "student_recurr": "master's student", "student_recurr": "first year  student", "student_recurr":"second year student", "student_recurr" : "third year student", "student_recurr": "fourth year student", "student_recurr": "fifth year student", "student_recurr":"graduate student", "student_recurr": "undergraduate student", "student_recurr": "international student", "student_recurr":"recurring student", "student_recurr":"continuing student", "student_recurr": "recurring undergraduate student", "student_recurr": "recurring graduate student", "student_recurr": "ongoing undergraduate student", "student_recurr":"ongoing graduate student"}
  - action_searchrecurringstudent
  - slot{"rinfo":"rstudent"}
  - utter_current_student
* good_thanks
  - utter_great
* yes_ido
  - utter_ask1
* on_campus{"campus_CSUDH":"campus"}
  - action_campus_info
  - slot{"campus_information":"campus_info"}
  - utter_campus_info
* campus_employment{"campus_employment_CSUDH":"employment"}
  - action_employment
  - slot{"campus_employment_stu":"campus_employment"}
  - utter_thank_you_uprogram
* goodbye
  - utter_goodbye
  - action_restart



## Story to view financial aid, enrollment, and computer science 500 then ending the program mixed up
* greet
  - utter_introduction
  - utter_introduction_r2
* choice_text{"choice":"text"}
  - action_choice_two
  - slot{"choice_two":"c_two"}
  - utter_ask_type_of_student
* student_type_two{"student_recurr":"ongoing student", "student_recurr": "freshman", "student_recurr":"sophmore", "student_recurr":"junior", "student_recurr":"senior", "student_recurr": "master's student", "student_recurr": "first year  student", "student_recurr":"second year student", "student_recurr" : "third year student", "student_recurr": "fourth year student", "student_recurr": "fifth year student", "student_recurr":"graduate student", "student_recurr": "undergraduate student", "student_recurr": "international student", "student_recurr":"recurring student", "student_recurr":"continuing student", "student_recurr": "recurring undergraduate student", "student_recurr": "recurring graduate student", "student_recurr": "ongoing undergraduate student", "student_recurr":"ongoing graduate student"}
  - action_searchrecurringstudent
  - slot{"rinfo":"rstudent"}
  - utter_current_student
* good_thanks
  - utter_great
* yes_ido
  - utter_ask1
* on_campus{"campus_CSUDH":"campus"}
  - action_campus_info
  - slot{"campus_information":"campus_info"}
  - utter_campus_info
* campus_map{"campus_map_CSUDH":"campus map"}
  - action_campusmap
  - slot{"campusMapCSUDH":"campus_mapCSUDH"}
  - utter_thank_you_uprogram
* goodbye
  - utter_goodbye
  - action_restart
