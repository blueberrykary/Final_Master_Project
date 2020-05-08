# API for CORONA VIRUS
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests
import json

import psycopg2
import psycopg2.extras
import traceback

class Action_CoronaTracker(Action):

    def name(self) -> Text:
        return "action_corona_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


            response = requests.get("https://covidtracking.com/api/counties").json()
            entities = tracker.latest_message['entities']
            print("Last Message Now", entities)
            state = None
            for e in entities:
                if e['entity'] == "state":
                    state = e['value']

            for data in response[" "]:
                if data["county"] == state.title():
                    print(data)


            dispatcher.utter_message(text = "results" + state.title())

            return []
