## Karen Salinas
## CSC 590
## Program to Search for Student, and redirects user to different branches
## within the stories.

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests
import json
import re

##==============================================================================#
##==============================================================================#
##==============================================================================#
##==============================================================================#
##=========================Selecting from incoming student=====================##
class Action_Search_IncomingStudent(Action):

    def name(self) -> Text:
        return "action_searchincomingstudent"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #istudent: incoming student slot
        istudent = tracker.get_slot("student_incoming")
        #iinfo: incoming student information
        iinfo = "incoming student"
        #uttering message when user inputs the type of student they are
        #in this case they are an incoming student
        dispatcher.utter_message("You are an {}".format(iinfo))
        #returning the slot for incoming student information
        return [SlotSet("iinfo", istudent)]
##==============================================================================#
##==============================================================================#
##==============================================================================#
##==============================================================================#
##====================Select the incoming program: undergraduate===============##
class Action_ProgramSearchUndergraduate(Action):

    def name(self) -> Text:
        return "action_search_undergraduateprogram"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #undergraduate program slot
        uprog = tracker.get_slot("program_undergrad")
        #the response from uprograms
        uprograms = "undergraduate program"
        #uttering message containing uprograms response from slot
        dispatcher.utter_message(text = "The following contains information over the {} program.".format(uprograms))
        #returning the slot for programs meant for incoming undergraduate
        return [SlotSet("uprograms", uprog)]
##==============================================================================#
##==============================================================================#
##==============================================================================#
##==============================================================================#
##==================Select the incoming program: graduate =====================##
class Action_ProgramSearch(Action):

    def name(self) -> Text:
        return "action_search_graduateprogram"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #graduate program slot
        gprog = tracker.get_slot("program_graduate")
        #the response from gprograms
        gprograms = "undergraduate program"
        #uttering message containing gprograms response from slot
        dispatcher.utter_message("The following contains information over the {} program.".format(gprograms))
        #returning the slot for programs meant for incoming graduate students
        return [SlotSet("gprograms", gprog)]
##==============================================================================#
##==============================================================================#
##==============================================================================#
##==============================================================================#
##========================Selecting from recurring student=====================##
class Action_Search_RecurrStudent(Action):

    def name(self) -> Text:
        return "action_searchrecurringstudent"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #rstudent: recurring student slot
        rstudent = tracker.get_slot("student_recurr")
        # rinfo: recurring student information
        rinfo = ""
        #uttering message when user inputs the type of student they are
        #in this case they are a recurring student
        dispatcher.utter_message("".format(rinfo))
        #returning the slot for recurring information
        return [SlotSet("rinfo", rstudent)]
##==============================================================================#
##==============================================================================#
##==============================================================================#
##==============================================================================#
##==============================================================================#
