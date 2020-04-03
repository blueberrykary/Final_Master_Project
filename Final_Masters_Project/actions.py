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
