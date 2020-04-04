from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests
import json
import re


# Import the getData module to fetch the data.
from dbConnect import getData

class ActionUser(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # query to select id 1, 'future student'
        # q = 'select type from user_type WHERE id = 1;'
        q = 'select type from user_type WHERE id = 1;'

        #pass the sql query to the getData method and store the results in `data` variable.
        data = getData(q)

        #use json.dump to take input and return json object.
        set_one = json.dumps(data[0][0], sort_keys=True, indent=4)
        #use replace() function to replase "" to empty.
        set = set_one.replace('"', '')

        #utter the message, which will be set, "Future Student"
        dispatcher.utter_message(text = set)

        pass
        # dispatcher.utter_button_template(set)
        # dispatcher.utter_custom_json({"payload":"future Student","data" : set})

# class FindUsers(Action):
#     def name(self) -> Text:
#         return "find_the_user"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#             buttons = []
#             for t in set:
#                 seet = set[t]
#                 payload: "/greet{\"seet\": \"" + seet.get()}"




        # q_one = 'select type from user_type WHERE id = 1;'
        #
        # data = getData(q_one)
        # set_one = json.dumps(data[0][0], sort_keys = True, indent = 4)
        # set_first = set_one.replace('"', '')
        #
        # q_two = 'select type from user_type WHERE id = 2;'
        # data = getData(q_two)
        # set_two = json.dumps(data[0][0], sort_keys = True, indent = 4)
        # set_second = set_two.replace('"', '')
        #
        # q_three = 'select type from user_type WHERE id = 3;'
        # data = getData(q_three)
        # set_three = json.dumps(data[0][0], sort_keys = True, indent = 4)
        # set_thrid = set_three.replace('"', '')

        # dispatcher.utter_message("Welcome to CSUDH. Which of the following best applies to you?")

            #
            # if set_first:
            #     dispatcher.utter_custom_json({"payload":set_first})
            # elif  set_second:
            #     dispatcher.utter_custom_json({"payload": set_second})
            # elif set_thrid:
            #     dispatcher.utter_custom_json({"payload":set_thrid})
            # else:
            #     pass




        # if(set_first or (set_second and set_thrid)):
        #     if()

        # sets = set_first, set_second, set_thrid

        # sets = set_first, set_second, set_thrid

        #
        # if(sets == set_first):
        #     dispatcher.utter_message({"payload":"Future Student", set_first})
        # else:
        #     dispatcher.utter
        #

        #switch statement for payload

#
# def find_users()
#
# class ActionUser2(Action):
#
#     def name(self) -> Text:
#         return "action_user_type_two"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         # query to select id 1, 'future student'
#         q = 'select type from user_type WHERE id = 2;'
#
#         #pass the sql query to the getData method and store the results in `data` variable.
#         data = getData(q)
#
#         #use json.dump to take input and return json object.
#         set_one = json.dumps(data[0][0], sort_keys=True, indent=4)
#         #use replace() function to replase "" to empty.
#         set = set_one.replace('"', '')
#         #utter the message, which will be set, "Future Student"
#         dispatcher.utter_message(text = set)
#
#         pass
#
# class ActionUser3(Action):
#
#     def name(self) -> Text:
#         return "action_user_type_three"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         # query to select id 1, 'future student'
#         q = 'select type from user_type WHERE id = 3;'
#
#         #pass the sql query to the getData method and store the results in `data` variable.
#         data = getData(q)
#
#         #use json.dump to take input and return json object.
#         set_one = json.dumps(data[0][0], sort_keys=True, indent=4)
#         #use replace() function to replase "" to empty.
#         set = set_one.replace('"', '')
#         #utter the message, which will be set, "Future Student"
#         dispatcher.utter_message(text = set)
#
#         pass
