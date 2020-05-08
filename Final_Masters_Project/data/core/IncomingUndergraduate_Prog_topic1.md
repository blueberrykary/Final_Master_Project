<!--
## Karen Salinas
## CSC 590
## Story for incoming undergraduate program
## contains the art program option with utter_art_loc
## and utter_art_img
-->
## Story 1a: The Incoming Undergraduate Student WANTS more details on the undergraduate programs with ART Program
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
* choose_incoming_undergrad_program{"program_undergrad":"undergraduate program", "program_undergrad":"undergrad program"}
  - action_search_undergraduateprogram
  - slot{"uprograms":"program_undergrad"}
  - utter_undergraduate
  - utter_undergraduate_program_options
* undergrad_programs_info{"program_undergrad_info":"undergrad program"}
  - action_display_undergradinfo
  - slot{"uprog_info":"uprog_iinfo"}
  - utter_option_program
* select_program_details_yes{"program_details_yes":"Of Course"}
  - action_prog_yes
  - slot{"program_yes":"prog_yes"}
  - utter_program_information
* art
  - utter_art_loc
  - utter_art_program
  - utter_curious_req
* select_requirements_yes{"program_requirement_details_yes":"Indeed"}
  - action_pro_req_yes
  - slot{"program_req_yes":"prog_req_yes"}
  - utter_ask_school
* select_school_info_yes{"school_info_yes":"Yessss"}
  - action_school_yes
  - slot{"schoolinfo_yes":"schooli_yes"}
  - utter_ask_steps
* select_stepstoapply_yes{"steps_apply_yes":"Steps yes"}
  - action_steps_apply_yes
  - slot{"steps_app_yes":"steps_yes"}
  - utter_thank_you_uprogram
* goodbye
  - utter_goodbye
  - action_restart


## Story 2a: The Incoming Undergraduate Student WANTS more details on the undergraduate requirements with ART Program
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
* choose_incoming_undergrad_program{"program_undergrad":"undergraduate program", "program_undergrad":"undergrad program"}
  - action_search_undergraduateprogram
  - slot{"uprograms":"program_undergrad"}
  - utter_undergraduate
  - utter_undergraduate_program_options
* undergrad_programs_info{"program_undergrad_info":"undergrad program"}
  - action_display_undergradinfo
  - slot{"uprog_info":"uprog_iinfo"}
  - utter_option_program
* select_program_details_yes{"program_details_yes":"Of Course"}
  - action_prog_yes
  - slot{"program_yes":"prog_yes"}
  - utter_program_information
* art
  - utter_art_loc
  - utter_art_program
  - utter_curious_req
* select_requirements_no{"program_requirement_details_no":"Definately Not"}
  - action_pro_req_no
  - slot{"program_req_no":"prog_req_no"}
  - utter_thank_you_uprogram
* goodbye
  - utter_goodbye
  - action_restart



<!--==============================================================-->
## Story 2b: The Incoming Undergraduate Student NOT want more details on requirements with ART Program
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
* choose_incoming_undergrad_program{"program_undergrad":"undergraduate program", "program_undergrad":"undergrad program"}
  - action_search_undergraduateprogram
  - slot{"uprograms":"program_undergrad"}
  - utter_undergraduate
  - utter_undergraduate_program_options
* undergrad_programs_info{"program_undergrad_info":"undergrad program"}
  - action_display_undergradinfo
  - slot{"uprog_info":"uprog_iinfo"}
  - utter_option_program
* select_program_details_no{"program_details_no":"Of Course Not"}
  - action_prog_no
  - slot{"program_no":"prog_no"}
  - utter_thank_you_uprogram
* goodbye
  - utter_goodbye
  - action_restart



## Story 2c: The Incoming Undergraduate Student NOT WANT details on school information with ART Program
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
* choose_incoming_undergrad_program{"program_undergrad":"undergraduate program", "program_undergrad":"undergrad program"}
  - action_search_undergraduateprogram
  - slot{"uprograms":"program_undergrad"}
  - utter_undergraduate
  - utter_undergraduate_program_options
* undergrad_programs_info{"program_undergrad_info":"undergrad program"}
  - action_display_undergradinfo
  - slot{"uprog_info":"uprog_iinfo"}
  - utter_option_program
* select_program_details_yes{"program_details_yes":"Of Course"}
  - action_prog_yes
  - slot{"program_yes":"prog_yes"}
  - utter_program_information
* art
  - utter_art_loc
  - utter_art_program
  - utter_curious_req
* select_requirements_yes{"program_requirement_details_yes":"Indeed"}
  - action_pro_req_yes
  - slot{"program_req_yes":"prog_req_yes"}
  - utter_ask_school
* select_school_info_no{"school_info_no":"Nooo"}
  - action_school_no
  - slot{"schoolinfo_no":"schooli_no"}
  - utter_thank_you_uprogram
* goodbye
  - utter_goodbye
  - action_restart


## Story 2d: The Incoming Undergraduate Student WANTS more details on the undergraduate programs with ART Program
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
* choose_incoming_undergrad_program{"program_undergrad":"undergraduate program", "program_undergrad":"undergrad program"}
  - action_search_undergraduateprogram
  - slot{"uprograms":"program_undergrad"}
  - utter_undergraduate
  - utter_undergraduate_program_options
* undergrad_programs_info{"program_undergrad_info":"undergrad program"}
  - action_display_undergradinfo
  - slot{"uprog_info":"uprog_iinfo"}
  - utter_option_program
* select_program_details_yes{"program_details_yes":"Of Course"}
  - action_prog_yes
  - slot{"program_yes":"prog_yes"}
  - utter_program_information
* art
  - utter_art_loc
  - utter_art_program
  - utter_curious_req
* select_requirements_yes{"program_requirement_details_yes":"Indeed"}
  - action_pro_req_yes
  - slot{"program_req_yes":"prog_req_yes"}
  - utter_ask_school
* select_school_info_yes{"school_info_yes":"Yessss"}
  - action_school_yes
  - slot{"schoolinfo_yes":"schooli_yes"}
  - utter_ask_steps
* select_stepstoapply_no{"steps_apply_no":"Steps no"}
  - action_steps_apply_no
  - slot{"steps_app_no":"steps_no"}
  - utter_thank_you_uprogram
* goodbye
  - utter_goodbye
  - action_restart
