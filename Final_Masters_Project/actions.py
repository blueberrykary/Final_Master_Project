from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionSearchUserOne(Action):

    def name(self) -> Text:
        return "action_search_student_one"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            user_one = tracker.get_slot("stud_one")
            student_num_one = "current student"
            dispatcher.utter_message("You selected that you are a {} at CSUDH".format(student_num_one))

            return[SlotSet("student_num_one", student_num_one)]

class ActionSearchUserTwo(Action):
    def name(self) -> Text:
        return "action_search_student_two"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            user_two = tracker.get_slot("stud_two")
            student_num_two = "Future Student"
            dispatcher.utter_message("This is the {}:{}".format(user_two, student_num_two))

            return[SlotSet("student_num_two", student_num_two)]

class ActionSearchUserThree(Action):
    def name(self) -> Text:
        return "action_search_instruct"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            user_three = tracker.get_slot("instruct")
            instruct_one = "Instructor"
            dispatcher.utter_message("This is the {}:{}".format(user_three, instruct_one))

            return[SlotSet("instruct_one", instruct_one)]

class ActionGoBack(Action):
    def name(self) -> Text:
        return "action_goback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            link = tracker.get_slot("link")
            redirected = "https://my.csudh.edu/psp/paaprd/EMPLOYEE/EMPL/h/?tab=PAPP_GUEST"
            dispatcher.utter_message("You have chosen {}, redirecting you to {}".format(link, redirected))

            return[SlotSet("link", redirected)]

class ActionGoBack2(Action):
    def name(self) -> Text:
        return "action_goback2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            link2 = tracker.get_slot("link2")
            redirected2 = "http://toromail.csudh.edu/"
            dispatcher.utter_message("You have chosen {}, redirecting you to {}.Make sure to enter your CSUDH username and password".format(link2, redirected2))

            return[SlotSet("link2", redirected2)]


class ActionGoBack3(Action):
    def name(self) -> Text:
        return "action_goback3"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            link3 = tracker.get_slot("link3")
            redirected3 = "https://toro.csudh.edu/webapps/login/"
            dispatcher.utter_message("You have chosen {}, redirecting you to {}.".format(link3, redirected3))

            return[SlotSet("link3", redirected3)]

class ActionGoBack4(Action):
    def name(self) -> Text:
        return "action_goback4"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            link4 = tracker.get_slot("link4")
            redirected4 = "https://www.csudh.edu/Assets/csudh-sites/academic-affairs/academic-calendar/docs/CSUDH_approved_academic_calendar_2019_2020.pdf"
            dispatcher.utter_message("You are now going to the {}. Redirecting you to {}".format(link4, redirected4))

            return[SlotSet("link4", redirected4)]


class ActionGoBack5(Action):
    def name(self) -> Text:
        return "action_goback5"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            link5 = tracker.get_slot("link5")
            redirected5 = "https://my.csudh.edu/psp/paaprd/EMPLOYEE/CDHPRD/c/DH_SA_CUSTOM.DH_SR_CLASS_SRCH.GBL?"
            dispatcher.utter_message("You are now being redirected to view the {} through {}.".format(link5, redirected5))

            return[SlotSet("link5", redirected5)]

class ActionScheduleAppt(Action):
    def name(self) -> Text:
        return "action_schedule_appt"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            Appt = tracker.get_slot("Appt")
            sched_appointment = "scheduling an appointment"
            dispatcher.utter_message("You will now go to {} in your designated department ".format(sched_appointment))

            return[SlotSet("sched_appointment", sched_appointment)]


#===================================================================================#
#==============================Actions for Scheduling Appointment===================#

class ActionUni(Action):

    def name(self) -> Text:
        return "action_schedule_university"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            uni = tracker.get_slot("school")
            universities = "University"
            dispatcher.utter_message("You selected that you are a {} at CSUDH".format(universities))

            return[SlotSet("uni", universities)]


class Action_ByMajor(Action):

    def name(self) -> Text:
        return "action_schedule_major"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            major = tracker.get_slot("By_Major")
            by_maj = "Major"
            dispatcher.utter_message("You selected that you are a {} at CSUDH".format(by_maj))

            return[SlotSet("major", by_maj)]

#==================Link with CompScie=====================#

# class Action_CompSci(Action):
#
#     def name(self) -> Text:
#         return "action_compsci"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         #dispatcher.utter_message(text="Hello World!")
#         dispatcher.utter_message(attachment={
#             "type": "link",
#             "payload": {
#                 "title": "Computer Science",
#                 "src": "https://cscadv.csudh.edu/"
#             }
#         })


#===== fix the go back button for going to utter_next =====#
#
# class Action_GoToUtterNext(Action):
#
#     def name(self) -> Text:
#         return "action_goto_utternext"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#             toUtterNext = tracker.get_slot("back")
#             back_to_UtterNext = "Going back to utter_next"
#             dispatcher.utter_message("You selected that you are a {} at CSUDH".format(toUtterNext))
#
#             return[SlotSet("toUtterNext", back_to_UtterNext)]
