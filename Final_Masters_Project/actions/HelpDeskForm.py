## Karen Salinas
## CSC 590
## Inquiry form for story in "Inquiries.md"

from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

##==============================================================================##
##==============================================================================##
##==============================================================================##
##==============================================================================##
##==========================Lead Form First-====================================##
class LeadFormFirstPart(FormAction):

    def name(self) -> Text:
        # Unique identifier of the form
        return "lead_form_p1"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        # A list of required slots that the form has to fill
        return ["inquiry"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "inquiry": [
                self.from_text(),
            ],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        # utter submit template
        dispatcher.utter_message(template="utter_more_details")
        return []
##==============================================================================##
##==============================================================================##
##==============================================================================##
##==============================================================================##
##==========================Lead Form Second====================================##
class LeadFormSecondPart(FormAction):
    def name(self) -> Text:
        return "lead_form_p2"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["details"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "details": [
                self.from_text(),
            ],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        return []
##==============================================================================##
##==============================================================================##
##==============================================================================##
##==============================================================================##
##==========================Lead Form Three=====================================##

class LeadFormThirdPart(FormAction):
    def name(self) -> Text:

        return "lead_form_p3"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["timeline", "name", "email", "phone"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "timeline": [
                self.from_text(),
            ],
            "name": [
                self.from_text(),
            ],
            "email": [
                self.from_text(),
            ],
            "phone": [
                self.from_text(),
            ],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        # utter submit response
        dispatcher.utter_message(template="utter_lead_q2")
        return []
