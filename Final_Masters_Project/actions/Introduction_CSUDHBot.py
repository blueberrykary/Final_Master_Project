## Karen Salinas
## CSC 590
## utter_introduction_r2

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
#This is meant for the introduction to select the "Inquiry" option
class ActionChoice_One(Action):

    def name(self) -> Text:
        return "action_choice_one"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            choice_one = tracker.get_slot("choice")
            c_one = "input an inquiry"
            dispatcher.utter_message("You selected to {} was your option".format(c_one))

            return[SlotSet("choice_one", c_one)]
##==============================================================================#
##==============================================================================#
##==============================================================================#
##==============================================================================#
#This is meant for the introduction to select the "Ask Questions to CSUDHBot" option
class ActionChoice_Two(Action):

    def name(self) -> Text:
        return "action_choice_two"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            choice_two = tracker.get_slot("choice")
            c_two = "ask questions to CSUDHBot"
            dispatcher.utter_message(" You selected to {} was your option. ".format(c_two))

            return[SlotSet("choice_two", c_two)]
##==============================================================================#
##==============================================================================#
##==============================================================================#
##==============================================================================#
##==============================================================================#
