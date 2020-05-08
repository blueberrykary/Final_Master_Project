## Story 1a: The Incoming Graduate Student WANTS more details on the undergraduate programs
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
