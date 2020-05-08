<!--
## Karen Salinas
## CSC 590
## Story for incoming graduate program
-->

## Story 1a: The Incoming Graduate Student WANTS more details on the grad programs
* greet
  - utter_introduction
  - utter_introduction_r2
* choice_text{"choice":"text"}
  - action_choice_two
  - slot{"choice_two":"c_two"}
  - utter_ask_type_of_student
* student_type_one{"student_incoming":"incoming student", "student_incoming":"prospective student", "student_incoming": "applicant", "student_incoming":"incoming undergraduate student", "student_incoming":"incoming undergrad student", "student_incoming": "incoming graduate student", "student_incoming": "incoming grad student", "student_incoming": "incoming freshman", "student_incoming":"transfer student", "student_incoming":"incoming first year student", "student_incoming":"incoming master's student"}
  - action_searchincomingstudent
  - slot{"iinfo":"istudent"}
  - utter_future_student
  - utter_future_student_r2
  - utter_future_student_r3
* choose_incoming_grad_program{"program_graduate":"graduate program", "program_graduate":"grad program"}
  - action_search_graduateprogram
  - slot{"gprograms":"program_graduate"}
  - utter_graduate
  - utter_graduate_program_options
* grad_program_info{"program_masters":"graduate program"}
  - action_graduatedd_program
  - slot{"graduate_program_details":"grad_program"}
  - utter_grad_option_program
* select_grad_program_details_yes{"program_grad_details_yes":"Yupp"}
  - action_grad_prog_yes
  - slot{"graduate_prog_yes":"grad_prog_yes"}
  - utter_grad_requirements
* select_grad_requirements_yes{"program_gradrequirement_details_yes":"Yas"}
  - action_grad_req_yes
  - slot{"graduate_progreq_yes":"grad_progreq_yes"}
  - utter_graduate_ask_school
* select_gradschool_yes{"view_gradschool_yes":"Si"}
  - action_gradinfo_yes
  - slot{"graduateinfo_yes":"gradinfo_yes"}
  - utter_grad_ask_steps
* select_gradsteps_yes{"view_grad_steps_yes":"yasss"}
  - action_grad_steps_apply_yes
  - slot{"graduatesteps_app_yes":"gradsteps_yes"}
  - utter_thank_you_uprogram
* goodbye
  - utter_goodbye
  - action_restart


  <!--========================================================-->
## Story 2a: The Incoming Graduate Student DOES NOT more details on the grad programs
* greet
  - utter_introduction
  - utter_introduction_r2
* choice_text{"choice":"text"}
  - action_choice_two
  - slot{"choice_two":"c_two"}
  - utter_ask_type_of_student
* student_type_one{"student_incoming":"incoming student", "student_incoming":"prospective student", "student_incoming": "applicant", "student_incoming":"incoming undergraduate student", "student_incoming":"incoming undergrad student", "student_incoming": "incoming graduate student", "student_incoming": "incoming grad student", "student_incoming": "incoming freshman", "student_incoming":"transfer student", "student_incoming":"incoming first year student", "student_incoming":"incoming master's student"}
  - action_searchincomingstudent
  - slot{"iinfo":"istudent"}
  - utter_future_student
  - utter_future_student_r2
  - utter_future_student_r3
* choose_incoming_grad_program{"program_graduate":"graduate program", "program_graduate":"grad program"}
  - action_search_graduateprogram
  - slot{"gprograms":"program_graduate"}
  - utter_graduate
  - utter_graduate_program_options
* grad_program_info{"program_masters":"graduate program"}
  - action_graduatedd_program
  - slot{"graduate_program_details":"grad_program"}
  - utter_grad_option_program
* select_grad_program_details_no{"program_grad_details_no":"Noope"}
  - action_grad_prog_no
  - slot{"graduate_prog_no":"grad_prog_no"}
  - utter_thank_you_uprogram
* goodbye
- utter_goodbye
- action_restart


## Story 2b: The Incoming Graduate Student DOES NOT to view requirements on the grad programs
* greet
  - utter_introduction
  - utter_introduction_r2
* choice_text{"choice":"text"}
  - action_choice_two
  - slot{"choice_two":"c_two"}
  - utter_ask_type_of_student
* student_type_one{"student_incoming":"incoming student", "student_incoming":"prospective student", "student_incoming": "applicant", "student_incoming":"incoming undergraduate student", "student_incoming":"incoming undergrad student", "student_incoming": "incoming graduate student", "student_incoming": "incoming grad student", "student_incoming": "incoming freshman", "student_incoming":"transfer student", "student_incoming":"incoming first year student", "student_incoming":"incoming master's student"}
  - action_searchincomingstudent
  - slot{"iinfo":"istudent"}
  - utter_future_student
  - utter_future_student_r2
  - utter_future_student_r3
* choose_incoming_grad_program{"program_graduate":"graduate program", "program_graduate":"grad program"}
  - action_search_graduateprogram
  - slot{"gprograms":"program_graduate"}
  - utter_graduate
  - utter_graduate_program_options
* grad_program_info{"program_masters":"graduate program"}
  - action_graduatedd_program
  - slot{"graduate_program_details":"grad_program"}
  - utter_grad_option_program
* select_grad_program_details_yes{"program_grad_details_yes":"Yupp"}
  - action_grad_prog_yes
  - slot{"graduate_prog_yes":"grad_prog_yes"}
  - utter_grad_requirements
* select_grad_requirements_no{"program_gradrequirement_details_no":"Nopee"}
  - action_grad_req_no
  - slot{"graduate_progreq_no":"grad_progreq_no"}
  - utter_thank_you_uprogram
* goodbye
  - utter_goodbye
  - action_restart



## Story 2c: The Incoming Graduate Student WANTS more details on the grad programs
* greet
  - utter_introduction
  - utter_introduction_r2
* choice_text{"choice":"text"}
  - action_choice_two
  - slot{"choice_two":"c_two"}
  - utter_ask_type_of_student
* student_type_one{"student_incoming":"incoming student", "student_incoming":"prospective student", "student_incoming": "applicant", "student_incoming":"incoming undergraduate student", "student_incoming":"incoming undergrad student", "student_incoming": "incoming graduate student", "student_incoming": "incoming grad student", "student_incoming": "incoming freshman", "student_incoming":"transfer student", "student_incoming":"incoming first year student", "student_incoming":"incoming master's student"}
  - action_searchincomingstudent
  - slot{"iinfo":"istudent"}
  - utter_future_student
  - utter_future_student_r2
  - utter_future_student_r3
* choose_incoming_grad_program{"program_graduate":"graduate program", "program_graduate":"grad program"}
  - action_search_graduateprogram
  - slot{"gprograms":"program_graduate"}
  - utter_graduate
  - utter_graduate_program_options
* grad_program_info{"program_masters":"graduate program"}
  - action_graduatedd_program
  - slot{"graduate_program_details":"grad_program"}
  - utter_grad_option_program
* select_grad_program_details_yes{"program_grad_details_yes":"Yupp"}
  - action_grad_prog_yes
  - slot{"graduate_prog_yes":"grad_prog_yes"}
  - utter_grad_requirements
* select_grad_requirements_yes{"program_gradrequirement_details_yes":"Yas"}
  - action_grad_req_yes
  - slot{"graduate_progreq_yes":"grad_progreq_yes"}
  - utter_graduate_ask_school
* select_gradschool_no{"view_gradschool_no":"Nay"}
  - action_gradinfo_no
  - slot{"graduate_progreq_no":"grad_progreq_no"}
  - utter_thank_you_uprogram
* goodbye
  - utter_goodbye
  - action_restart



## Story 2d: The Incoming Graduate Student WANTS more details on the grad programs
* greet
  - utter_introduction
  - utter_introduction_r2
* choice_text{"choice":"text"}
  - action_choice_two
  - slot{"choice_two":"c_two"}
  - utter_ask_type_of_student
* student_type_one{"student_incoming":"incoming student", "student_incoming":"prospective student", "student_incoming": "applicant", "student_incoming":"incoming undergraduate student", "student_incoming":"incoming undergrad student", "student_incoming": "incoming graduate student", "student_incoming": "incoming grad student", "student_incoming": "incoming freshman", "student_incoming":"transfer student", "student_incoming":"incoming first year student", "student_incoming":"incoming master's student"}
  - action_searchincomingstudent
  - slot{"iinfo":"istudent"}
  - utter_future_student
  - utter_future_student_r2
  - utter_future_student_r3
* choose_incoming_grad_program{"program_graduate":"graduate program", "program_graduate":"grad program"}
  - action_search_graduateprogram
  - slot{"gprograms":"program_graduate"}
  - utter_graduate
  - utter_graduate_program_options
* grad_program_info{"program_masters":"graduate program"}
  - action_graduatedd_program
  - slot{"graduate_program_details":"grad_program"}
  - utter_grad_option_program
* select_grad_program_details_yes{"program_grad_details_yes":"Yupp"}
  - action_grad_prog_yes
  - slot{"graduate_prog_yes":"grad_prog_yes"}
  - utter_grad_requirements
* select_grad_requirements_yes{"program_gradrequirement_details_yes":"Yas"}
  - action_grad_req_yes
  - slot{"graduate_progreq_yes":"grad_progreq_yes"}
  - utter_graduate_ask_school
* select_gradschool_yes{"view_gradschool_yes":"Si"}
  - action_gradinfo_yes
  - slot{"graduateinfo_yes":"gradinfo_yes"}
  - utter_grad_ask_steps
* select_gradsteps_no{"view_grad_steps_no":"nooooo"}
  - action_grad_steps_apply_no
  - slot{"graduatesteps_app_no":"gradsteps_no"}
  - utter_thank_you_uprogram
* goodbye
  - utter_goodbye
  - action_restart
