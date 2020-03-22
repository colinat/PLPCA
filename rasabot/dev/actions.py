# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

import csv
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionGetSentiment(Action):

    def name(self) -> Text:
        return "action_respond_sentiment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        aspect = tracker.get_slot("aspect_type")
        data_list = [["SN", "Name", "Contribution"],
                     [1, "Linus Torvalds", "Linux Kernel"],
                     [2, "Tim Berners-Lee", "World Wide Web"],
                     [3, "Guido van Rossum", "Python Programming"]]
        with open('innovators.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerows(data_list)
        dispatcher.utter_message("Hello! I am feeling good on {}".format(aspect))

        return []
