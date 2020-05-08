<!--
## Karen Salinas
## CSC 590
## Story mixed up story with three elements
-->

## Story to view campus tour
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
* university_enrollment{"uni_enroll":"enrollment"}
  - action_Eenrollment
  - slot{"university_enroll":"unii_enrollment"}
  - utter_enrollment
* ask_a_question
  - utter_ask2
* financial_aid_application{"FAFSA_APP":"FAFSA", "FAFSA_APP":"financial aid"}
  - action_FAFSA
  - slot{"fafsa_appp":"fafsa_application"}
  - utter_financial_aid
* ask_a_question
  - utter_ask3
* course_description{"getting_course": "computer science", "getting_course":"comp sci", "getting_course": "comp science"}
  - action_view_cs_course
  - slot{"course_end":"course_start"}
  - utter_computerscience_option
* Summer2020
  - utter_classes_summer_20201
* courses_summer2020{"summer_2020_course1":"csc 500"}
  - action_view_summer2020
  - slot{"summer_2020c1":"summer_c1"}
  - utter_thank_you_uprogram
* goodbye
  - utter_goodbye
  - action_restart



## Story to view financial aid, enrollment, and computer science 501 then ending the program mixed up
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
* university_enrollment{"uni_enroll":"enrollment"}
  - action_Eenrollment
  - slot{"university_enroll":"unii_enrollment"}
  - utter_enrollment
* ask_a_question
  - utter_ask2
* financial_aid_application{"FAFSA_APP":"FAFSA", "FAFSA_APP":"financial aid"}
  - action_FAFSA
  - slot{"fafsa_appp":"fafsa_application"}
  - utter_financial_aid
* ask_a_question
  - utter_ask3
* course_description{"getting_course": "computer science", "getting_course":"comp sci", "getting_course": "comp science"}
  - action_view_cs_course
  - slot{"course_end":"course_start"}
  - utter_computerscience_option
* Summer2020
  - utter_classes_summer_20201
* courses_summer20201{"summer_2020_course2":"csc 501"}
  - action_view_summer20202
  - slot{"summer_2020c2":"summer_c2"}
  - utter_thank_you_uprogram
* goodbye
  - utter_goodbye
  - action_restart
