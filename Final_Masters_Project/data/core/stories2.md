## schedule appointment University
* schedule_appointment{"Appt":"Schedule"}
  - action_schedule_appt
  - slot{"sched_appointment":"sched_appointment"}
  - utter_schedule
* University{"school":"Universities"}
  - action_schedule_university
  - slot{"uni":"universities"}
  - utter_schedule
* By_Major{"school":"Major"}
  - action_schedule_major
  - slot{"major":"by_maj"}
* search_student_one{"stud_one":"current student"}
  - action_search_student_one
  - slot{"student_num_one":"Current Student"}
  - utter_next

## schedule appoint By Major
* schedule_appointment{"Appt":"Schedule"}
  - action_schedule_appt
  - slot{"sched_appointment":"sched_appointment"}
  - utter_schedule
* By_Major{"school":"Major"}
  - action_schedule_major
  - slot{"major":"by_maj"}
* University{"school":"Universities"}
  - action_schedule_university
  - slot{"uni":"universities"}
  - utter_schedule
* search_student_one{"stud_one":"current student"}
  - action_search_student_one
  - slot{"student_num_one":"Current Student"}
  - utter_next
<!-- 
## schedule by major -- computer Science

* CompSci{"Appt":"Computer Science"}
  - action_compsci
  - utter_schedule_bymajor -->
