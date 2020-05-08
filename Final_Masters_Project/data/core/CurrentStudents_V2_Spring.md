<!--
## Karen Salinas
## CSC 590
## Story for fafsa, enrollment, computer science mixed up for Spring 2020
-->

## Story to view financial aid, enrollment, and computer science 585 then ending the program mixed up SPRING term
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
* Spring2020
  - utter_classes_spring_2020
* courses_spring20201{"spring_2020_course2":"csc 585"}
  - action_view_spring20202
  - slot{"spring_2020c2":"spring_c2"}
  - utter_thank_you_uprogram
* goodbye
  - utter_goodbye
  - action_restart


<!--===================================================-->
<!--===================================================-->

## Story to view financial aid, enrollment, and computer science 590 then ending the program mixed up SPRING term
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
* Spring2020
  - utter_classes_spring_2020
* courses_spring2020{"spring_2020_course1":"csc 590"}
  - action_view_spring2020
  - slot{"spring_2020c1":"spring_c1"}
  - utter_thank_you_uprogram
* goodbye
  - utter_goodbye
  - action_restart


<!--===================================================-->
<!--===================================================-->


<!--===================================================-->
<!--===================================================-->

## Story to view financial aid, enrollment, and computer science 582 then ending the program mixed up SPRING term
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
* Spring2020
  - utter_classes_spring_2020
* courses_spring20202{"spring_2020_course3":"csc 582"}
  - action_view_spring20203
  - slot{"spring_2020c3":"spring_c3"}
  - utter_thank_you_uprogram
* goodbye
  - utter_goodbye
  - action_restart


<!--===================================================-->
<!--===================================================-->
