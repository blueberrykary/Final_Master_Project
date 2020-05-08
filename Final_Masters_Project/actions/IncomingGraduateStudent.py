## Karen Salinas
## CSC 590
## For incoming graduate student
## Using data from the database
from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests
import json
import re
import sqlalchemy
from dbConnect import getData


class Action_GraduateProgramed(Action):

    def name(self) -> Text:
        return "action_graduatedd_program"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #school information slot
        grad_program = tracker.get_slot("program_masters")
        #the response from uschool_iinfo
        message = "CSUDH offers a wide selection of outstanding degrees that reflect today’s in-demand fields. Our degree programs offer a well-rounded curriculum that combines rigorous academics with a practical education."
        message2 = "CSUDH offers 44 undergraduate majors with high-demand options or concentrations recognized for their quality, well-rounded curricula, and balance of classroom learning and practical experience."
        #select the school's department information
        q = 'SELECT dept.department_name FROM school as s INNER JOIN belongs_to_school_depart as b_dept ON s.school_id = b_dept.school_id INNER JOIN department as dept ON b_dept.department_id = dept.department_id'
        #pass the sql query to the getData method and store the results in `data` variable.
        data = getData(q)
        #list out the departments
        set_one = str(data[0][0])
        set_two = str(data[1][0])
        set_three = str(data[2][0])
        set_four = str(data[3][0])
        set_five = str(data[4][0])
        set_six = str(data[5][0])
        #combine the departments with print out message
        set_combined  = set_one + "\n\n" + set_two + "\n\n" + set_three + "\n\n" + set_four + "\n\n" + set_five + "\n\n" + set_six
        #combine all the messages to one
        ult_message = message + "\n\n" + message2 + "\n\n" + set_combined + "\n\n"
        graduate_program_details = ult_message
        #uttering message containing the school response from slot
        dispatcher.utter_message(text="{}".format(graduate_program_details))
        #returning the slot for school information meant for incoming graduate students
        return [SlotSet("graduate_program_details", grad_program)]
#
# ##=================================DO NOT go to program details?=================#
# class Action_UndergradProgramNo(Action):
#
#     def name(self) -> Text:
#         return "action_prog_no"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         #school information slot
#         prog_no = tracker.get_slot("program_details_no")
#         #the response from uschool_iinfo
#         program_no = "no"
#         #uttering message containing the school response from slot
#         dispatcher.utter_message(text="You said {}".format(program_no))
#
#         #returning the slot for school information meant for incoming graduate students
#         return [SlotSet("program_no", prog_no)]
# ##==============================================================================#
# ##==============================================================================#
# ##==============================================================================#
# ##==============================================================================#
# ##==============================Go to the program requirements?=================#
##========FILL THIS ONE IN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=============#
class Action_GradProg_Yes(Action):

    def name(self) -> Text:
        return "action_grad_prog_yes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #school information slot
        grad_prog_yes = tracker.get_slot("program_grad_details_yes")

        message = "Pick up to 21 programs that match your needs, goals and personality and the research you have done on different schools. You will then need to make a time line for each program."
        view_more_programs = '<a href ="https://www.csudh.edu/gsr/graduate-studies/degree-programs/">View Programs</a>'

        overall = message + "<br/><br/>" + view_more_programs
        graduate_prog_yes = overall
        #uttering message containing the school response from slot
        dispatcher.utter_message(text="{}".format(graduate_prog_yes))

        #returning the slot for school information meant for incoming graduate students
        return [SlotSet("graduate_prog_yes", grad_prog_yes)]

##=================================DO NOT go to program requirements?=================#
class Action_GradProg_No(Action):

    def name(self) -> Text:
        return "action_grad_prog_no"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #school information slot
        grad_prog_no = tracker.get_slot("program_grad_details_no")
        #the response from uschool_iinfo
        graduate_prog_no = ""
        #uttering message containing the school response from slot
        dispatcher.utter_message(text="".format(graduate_prog_no))

        #returning the slot for school information meant for incoming graduate students
        return [SlotSet("graduate_prog_no", grad_prog_no)]
# ##==============================================================================#
# ##==============================================================================#
# ##==============================================================================#
class Action_GradReqYes(Action):

    def name(self) -> Text:
        return "action_grad_req_yes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #school information slot
        grad_progreq_yes = tracker.get_slot("program_gradrequirement_details_yes")
        #the response from uschool_iinfo
        req = "Completion of a four-year college course of study and an acceptable baccalaureate degree from an institution accredited by a regional accrediting association or completion of equivalent academic preparation as determined by appropriate campus authorities. <br> Good academic standing at the last college or university attended. <br> A grade point average of at least 2.5 (A = 4.0) in the last 60 semester (90 quarter) units attempted. <br> Satisfactory adherence to the professional, personal, scholastic, and other standards for graduate study, including qualifying examinations, as appropriate campus authorities may prescribe."

        req_info = '<a href ="https://www.csudh.edu/gsr/graduate-studies/graduate-admission/">Graduate Requirements</a>'

        overall = req + "<br/>" + req_info
        graduate_progreq_yes = overall
        #uttering message containing the school response from slot
        dispatcher.utter_message(text="{}".format(graduate_progreq_yes))

        #returning the slot for school information meant for incoming graduate students
        return [SlotSet("graduate_progreq_yes", grad_progreq_yes)]

##=================================DO NOT go to program requirements?=================#
class Action_GradReqNo(Action):

    def name(self) -> Text:
        return "action_grad_req_no"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #school information slot
        grad_progreq_no = tracker.get_slot("program_gradrequirement_details_no")
        #the response from uschool_iinfo
        graduate_progreq_no = ""
        #uttering message containing the school response from slot
        dispatcher.utter_message(text="".format(graduate_progreq_no))

        #returning the slot for school information meant for incoming graduate students
        return [SlotSet("graduate_progreq_no", grad_progreq_no)]

# ##==============================================================================#
# ##==============================================================================#
##=============================================================================##
##=============================================================================##
##=============================================================================##

class Action_GradSchoolInfo_Yes(Action):

    def name(self) -> Text:
        return "action_gradinfo_yes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #school information slot
        gradinfo_yes = tracker.get_slot("view_gradschool_yes")

        why_grad = " REASONS TO GO TO GRAD SCHOOL: <br/> <br/>A requirement for the career; for example law, medicine, social work, occupational therapy, counseling. <br/><br/> To move up in a field of work or earn more income; e.g., nursing, business management, teaching, public administration. <br/><br/> To prepare for a research career or to teach in higher education. <br/><br/>  To change careers <br/><br/> For personal growth"
        how_to_begin = "\n\n HOW TO BEGIN CONSIDERATION TO GRAD SCHOOL: <br/><br/> Consider the reasons you want to attend graduate school. Evaluate your interests, skills, values and goals in determining the program that suits you best. Think about how this decision will affect you and other people in your life. You want to spend a lot of time making an informed decision. <br/> The Career Center can help:<br/><br/> Attend a Graduate School Search Workshop offered by our office <br/> Attend the annual Graduate School Fair sponsored by the Career Center <br/> Talk with a Career Coach <br/> Visit the Career Center's Career Resource Library\n\n"
        admin_req = "ADMISSION REQUIREMENTS <br/><br/> May include the following:<br/><br/> Baccalaureate degree <br/>Minimum grade point average (cumulative or last 60 units) <br/>Minimum score on a standardized entrance examination (e.g., GRE, GMAT, MSAT) <br/> Letters of recommendation (usually 3) <br/> Experience in the field\n\n"
        app_process = "APPLICATION PROCESS<br/><br/>Complete Application - May be required for university and individual program.<br/><br/> Application Fee (usually $50 to $75)<br/> Transcripts - Official transcripts to be sent from each from college or university attended. <br/>  Statement of Purpose <br/> Letters of Recommendation (usually 3, typically professors) <br/> Required Entrance Examinations - Prepare for and take any assessment required. There are many preparation courses you can take with a variety of costs. Following are the websites for some of the most common exams: <br/><br/>"

        gre = '<a href ="http://www.ets.org/gre">GRE</a>'
        lsat = '<a href ="https://www.lsac.org/lsat">LSAT</a>'
        pharm = '<a href ="http://www.pcat.info/">PCAT</a>'
        gmat = '<a href ="https://www.mba.com/">GMAT</a>'
        for_more1 = "For more information over graduate school, please go to the link: "
        for_more = '<a href ="https://www.csudh.edu/career-center/students/graduate-school/">Grad School Information</a>'

        overall = why_grad + how_to_begin + admin_req + app_process + gre + "<br/>" + lsat + "<br/>" + pharm + "<br/>" + gmat + "<br/>" + for_more1 + for_more
        graduateinfo_yes = overall

        dispatcher.utter_message(text="{}".format(graduateinfo_yes))

        #returning the slot for school information meant for incoming graduate students
        return [SlotSet("graduateinfo_yes", gradinfo_yes)]

##=================================DO NOT go to program requirements?=================#
class Action_GradSchoolInfo_No(Action):

    def name(self) -> Text:
        return "action_gradinfo_no"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #school information slot
        grad_progreq_no = tracker.get_slot("view_gradschool_no")
        #the response from uschool_iinfo
        graduate_progreq_no = ""
        #uttering message containing the school response from slot
        dispatcher.utter_message(text="".format(graduate_progreq_no))

        #returning the slot for school information meant for incoming graduate students
        return [SlotSet("graduate_progreq_no", grad_progreq_no)]
##=============================================================================##
##=============================================================================##
#=============================================================================##
#=============================================================================##
##=================================Go to the program details?=================#
class Action_GradStepsYes(Action):

    def name(self) -> Text:
        return "action_grad_steps_apply_yes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #school information slot
        gradsteps_yes = tracker.get_slot("view_grad_steps_yes")
        #the response from uschool_iinfo
        how_to = '<a href ="https://www.csudh.edu/gsr/graduate-studies/graduation/how-to-apply/">How To Apply</a>'
        when_to = '<a href ="https://www.csudh.edu/gsr/graduate-studies/graduation/when-to-apply/">When To Apply</a>'
        candinacy_info = "The degree is awarded upon the satisfactory completion of all state and university requirements, the specific requirements for the particular program, the recommendation of the appropriate graduate adviser and program coordinator (advancement to candidacy), and the approval of the faculty and Dean of Graduate Studies.<br/>"
        how_to_know = '<a href ="https://www.csudh.edu/gsr/graduate-studies/graduation/requirements/advancement-to-candidacy/">Advancement To Candidancy</a>'
        gwar = '<a href ="https://www.csudh.edu/gsr/graduate-studies/graduation/requirements/gwar/">GWAR</a>'
        apply_here = '<a href ="https://www2.calstate.edu/apply/graduate">Apply Here</a>'
        time_lim = "Upon acceptance, all requirements for the master's degree, including all course work on the student's approved program of study must be completed within five years (some programs permit seven years). This time limit commences with the semester of the earliest course used on the student's program of study."

        message = candinacy_info + "<br/>" + time_lim + "<br/><br/>" + how_to + "<br/>" + apply_here + "<br/>" + when_to + "<br/>" + how_to_know + "<br/>" + gwar

        graduatesteps_app_yes = message
        #uttering message containing the school response from slot
        dispatcher.utter_message(text="{}".format(graduatesteps_app_yes))

        #returning the slot for school information meant for incoming graduate students
        return [SlotSet("graduatesteps_app_yes", gradsteps_yes)]

##=================================DO NOT go to program details?=================#
class Action_GradStepsNo(Action):

    def name(self) -> Text:
        return "action_grad_steps_apply_no"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #school information slot
        gradsteps_no = tracker.get_slot("view_grad_steps_no")
        #the response from uschool_iinfo
        graduatesteps_app_no = ""
        #uttering message containing the school response from slot
        dispatcher.utter_message(text="".format(graduatesteps_app_no))

        #returning the slot for school information meant for incoming graduate students
        return [SlotSet("graduatesteps_app_no", gradsteps_no)]
##==============================================================================#
