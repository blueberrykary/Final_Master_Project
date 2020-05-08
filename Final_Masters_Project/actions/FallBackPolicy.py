# ## Karen Salinas
# ## CSC 590
# ## Fallback Policy
# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import UserUtteranceReverted
# from rasa_sdk.events import SlotSet
#
# ## Did not use the fallback policy since it was causing problems with my program
# class ActionFallBackPolicy(Action):
#
#     def name(self) -> Text:
#         return "action_custom_fallback"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message('utter_custom', tracker)
#
#         return [UserUtteranceReverted()]
