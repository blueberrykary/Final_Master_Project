## Karen Salinas
## CSC 590
## For incoming undergraduate student
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
##==============================================================================#
##==============================================================================#
##==============================================================================#
##======================Display Undergraduate Program Information =============##
class Action_UnderProgramSearchInfo(Action):

    def name(self) -> Text:
        return "action_display_undergradinfo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #undergraduate information program slot
        uprog_info = tracker.get_slot("program_undergrad_info")
        ## message and message 2 will be combined with query 'q'
        message = "CSUDH offers a wide selection of outstanding degrees that reflect today’s in-demand fields. Our degree programs offer a well-rounded curriculum that combines rigorous academics with a practical education."
        message2 = "CSUDH offers 44 undergraduate majors with high-demand options or concentrations recognized for their quality, well-rounded curricula, and balance of classroom learning and practical experience."
        #select the school's department and show its name.
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
        #the response from uprog_iinfo
        uprog_iinfo = ult_message
        # utters message as {} along with link
        dispatcher.utter_message(text="{}".format(uprog_iinfo))
        #store the message into slot
        return [SlotSet("uprog_info", uprog_iinfo)]
##==============================================================================#
##==============================================================================#
##==============================================================================#
##=================================Go to the program details====================#

class Action_UndergradProgramYes(Action):

    def name(self) -> Text:
        return "action_prog_yes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        prog_yes = tracker.get_slot("program_details_yes")
        ## prints empty message
        message =  ""
        ## programs are listed in the utterance since it provides payloads
        #the response from program_yes
        program_yes = message
        #uttering message containing the program response from slot
        dispatcher.utter_message(text="".format(program_yes))
        #returning the slot for program meant for incoming undergraduate students
        return [SlotSet("program_yes", prog_yes)]

##=================================DO NOT go to program details==================#
class Action_UndergradProgramNo(Action):

    def name(self) -> Text:
        return "action_prog_no"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ##prints an empty message or program_no
        prog_no = tracker.get_slot("program_details_no")
        #the response from program_no, but is empty
        program_no = ""
        #uttering message containing the program no response from slot
        dispatcher.utter_message(text="".format(program_no))
        #returning the slot for program_no meant for incoming undergraduate students
        return [SlotSet("program_no", prog_no)]
##==============================================================================#
##==============================================================================#
##==============================================================================#
##=================================Go to the program requirement================#
class Action_UndergradReqYes(Action):

    def name(self) -> Text:
        return "action_pro_req_yes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #program requirement slot
        prog_req_yes = tracker.get_slot("program_requirement_details_yes")
        ## messages combined to be uttered
        message = "CSUDH is not impacted for First-Time Freshmen Applicants. "
        message2 = "The university's criteria for admission as a first–time freshman are met if a student \n"
        message3 = "1. Is a high school graduate; "
        message4 = "2. Has a qualifiable eligibility index; and"
        message5 = "3. Has completed with grades of C or better each of the courses in the comprehensive pattern of college preparatory subject requirements. Courses must be completed prior to the first enrollment in the California State University."
        out = message + "\n\n" + message2 + "\n\n" + message3 + "\n\n" + message4 + "\n\n" + message5 + "\n\n"
        program_req_yes = out
        #uttering message containing program requirement yes response from slot
        dispatcher.utter_message(text="{}".format(program_req_yes))
        #returning the slot for program requirement yes for incoming undergraduate students
        return [SlotSet("program_req_yes", prog_req_yes)]

##=================================DO NOT go to program requirements=================#
class Action_UndergradReqNo(Action):

    def name(self) -> Text:
        return "action_pro_req_no"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #school information slot
        prog_req_no = tracker.get_slot("program_requirement_details_no")
        #the response from uschool_iinfo
        program_req_no = ""
        #uttering message containing the school response from slot
        dispatcher.utter_message(text="".format(program_req_no))
        #returning the slot for school information meant for incoming graduate students
        return [SlotSet("program_req_no", prog_req_no)]
##==============================================================================#
##==============================================================================#
##==============================================================================#
##=======================Go to the program School Information===================#
class Action_SchoolInfoYes(Action):

    def name(self) -> Text:
        return "action_school_yes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #school information slot
        schooli_yes = tracker.get_slot("school_info_yes")
        ## query to get school information from information table
        q = 'select  i.description from school as sc INNER JOIN contains_info as ci ON ci.school_id = sc.school_id INNER JOIN information as i ON ci.info_id = i.info_id'
        #pass the sql query to the getData method and store the results in `data` variable.
        data = getData(q)
        #Print out school information
        details = "School Information"
        seperator = "========================================="
        set_one = str(data[0][0]) + "\n\n" +  str(data[1][0])
        set_combined = details + "\n" + seperator + "\n" +  set_one + "\n"
        #the response from school information yes
        schoolinfo_yes = set_combined
        #uttering message containing the school information response from slot
        dispatcher.utter_message(text="{}".format(schoolinfo_yes))
        #returning the slot for school information meant for incoming graduate students
        return [SlotSet("schoolinfo_yes", schooli_yes)]

##=================================DO NOT go to program requirements?=================#
class Action_SchoolInfoNo(Action):

    def name(self) -> Text:
        return "action_school_no"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #school information slot
        schooli_no = tracker.get_slot("school_info_no")
        #the response from school information no, but is empty
        schoolinfo_no = ""
        #uttering message containing the school information no response from slot
        dispatcher.utter_message(text="".format(schoolinfo_no))
        #returning the slot for school information no  meant for incoming graduate students
        return [SlotSet("schoolinfo_no", schooli_no)]
##==============================================================================#
##==============================================================================#
##==============================================================================#
##=================================Go to the program details?===================#
class Action_Steps_to_apply_yes(Action):

    def name(self) -> Text:
        return "action_steps_apply_yes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #school information slot
        steps_yes = tracker.get_slot("steps_apply_yes")
        #the response from steps to apply
        q = 'select si.step_name, si.step_description from school as sc INNER JOIN views_steps as v ON v.school_id = v.school_id INNER JOIN steps_info as si ON v.steps_id = si.steps_id where si.steps_id = 1 OR si.steps_id = 2 OR si.steps_id = 3 OR si.steps_id = 4'
        #pass the sql query to the getData method and store the results in `data` variable.
        data = getData(q)
        #Print out the steps to apply for undergraduate students
        details = "The following are steps to apply to CSUDH for Incoming Undergraduate Students"
        set_one = str(data[0][0]) + " : " +  str(data[0][1])
        set_two = str(data[1][0]) + " : " + str(data[1][1])
        set_three = str(data[2][0]) + " : " + str(data[2][1])
        set_four = str(data[3][0]) + " : " + str(data[3][1])
        ## combining all of the queries together to create one overall utterance
        set_combined = details + "\n" + set_one + "\n\n" + set_two + "\n\n" + set_three + "\n\n" + set_four
        ## combined for steps to apply yes
        steps_app_yes = set_combined
        #uttering message containing the steps to apply yes response from slot
        dispatcher.utter_message(text="{}".format(steps_app_yes))
        #returning the slot for steps to apply yes meant for incoming graduate students
        return [SlotSet("steps_app_yes", steps_yes)]

##=================================DO NOT go to program details?=================#
class Action_Steps_to_apply_no(Action):

    def name(self) -> Text:
        return "action_steps_apply_no"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        steps_no = tracker.get_slot("steps_apply_no")
        #the response for steps app no, with empty message
        steps_app_no = ""
        #uttering message containing the steps app no response from slot
        dispatcher.utter_message(text="".format(steps_app_no))
        #returning the slot for school app no meant for incoming graduate students
        return [SlotSet("steps_app_no", steps_no)]
##==============================================================================#
##==============================================================================#
##==============================================================================#
##==============================================================================#
##==============================================================================#
