# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

import csv
import numpy as np
import pandas as pd
import pandasql as ps

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
        listOfAspects = ['sales','earnings','op_costs','products_services','organic_expansion','acquisitions','competition',
                         'op_risks','debt']
        
        # return if aspect not found among valid list
        if aspect not in listOfAspects:
            # return bot's response
            dispatcher.utter_message("I'm sorry, but {} is not a valid aspect that I can handle in my current state.".format(aspect))
            return []
        
        else:
            # read from BERT model output contained in csv file
            df = pd.read_csv('predicted_Western Union Co_20170502-Text.csv', delimiter = ',')

            # threshold score to pick out sentences related to that aspect
            threshold = 0.6

            # extract out sentences associated with specified aspect
            sql = f"SELECT Sentiment, Emotion, {aspect} FROM df where {aspect} > {threshold}"
            subquery = ps.sqldf(sql, locals())
            subquery2 = ps.sqldf("SELECT Sentiment, COUNT(Sentiment) As count FROM subquery GROUP BY Sentiment", locals())

            # get total number of sentences related to that aspect
            result = ps.sqldf("SELECT sum(count) as total FROM subquery2", locals())
            num_sent = result.iloc[0,0]

            # exception handling: initialise to zero count if no result retrieved in earlier step
            if num_sent is None:
                num_sent = 0
                # return bot's response
                dispatcher.utter_message("Unfortunately, it seems there isn't any mentions relating to {}.".format(aspect))
            else:       
                # get associated sentiment to that aspect
                result = ps.sqldf("SELECT Sentiment, max(count) FROM subquery2", locals())
                sentiment = result.iloc[0,0]

                if sentiment is not None:
                    sentiment = sentiment[2:]
                    count = result.iloc[0,1]
                    pct = round(count/num_sent*100,0)
                    level = ""
                    if pct > 90:
                        level = "extremely"
                    elif pct > 70:
                        level = "very"
                    elif pct > 50:
                        level = "generally"
                    else:
                        level = "mildly"
                # exception handling: initialise to neutral sentiment if not able to be retrieved.
                else:
                    sentiment = "Neutral"
                # return bot's response
                dispatcher.utter_message("There are {} mentions associated with {}. They are {} {} (~{}%).".format(num_sent, aspect, level, sentiment, pct))
            return []
        
        
class ActionGetSentence(Action):

    def name(self) -> Text:
        return "action_respond_sentence"

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
    
    