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
from rasa_sdk.events import FollowupAction

filename = 'data/output.csv'
listOfAspects = ['sales','earnings','op_costs','products_services','organic_expansion','acquisitions','competition','op_risks','debt']
listOfSents = ['Positive','Neutral','Negative']

class ActionGetSentiment(Action):

    def name(self) -> Text:
        return "action_respond_sentiment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        aspect = tracker.get_slot("aspect_type")

        
        # return if aspect not found among valid list
        if aspect not in listOfAspects:
            # return bot's response
            dispatcher.utter_message("Entity: {}".format(aspect))
            dispatcher.utter_message("Intent: Get Sentiment")
            dispatcher.utter_message("{} isn't a valid aspect I can handle.".format(aspect))
            return [FollowupAction("utter_suggest_aspect")]
        
        else:
            # read from BERT model output contained in csv file
            df = pd.read_csv(filename, delimiter = ',')

            # threshold score to pick out sentences related to that aspect
            threshold = 0.6

            # extract out sentences associated with specified aspect
            #sql = f"SELECT Sentiment, {aspect} FROM df where {aspect} > {threshold}" # replaced
            
            sql = f"SELECT Sentiment, Aspect FROM df where Aspect LIKE '%{aspect}%'" # newly ammended code
            
            subquery = ps.sqldf(sql, locals())
            subquery2 = ps.sqldf("SELECT Sentiment, COUNT(Sentiment) As count FROM subquery GROUP BY Sentiment", locals())

            # get total number of sentences related to that aspect
            result = ps.sqldf("SELECT sum(count) as total FROM subquery2", locals())
            num_sent = result.iloc[0,0]

            # exception handling: initialise to zero count if no result retrieved in earlier step
            if num_sent is None:
                num_sent = 0
                # return bot's response
                dispatcher.utter_message("Entity: {}".format(aspect))
                dispatcher.utter_message("Intent: Get Sentiment.")
                dispatcher.utter_message("Unfortunately, it seems there isn't any notable mentions relating to {}.".format(aspect))
            else:       
                # get associated sentiment to that aspect
                result = ps.sqldf("SELECT Sentiment, max(count) FROM subquery2", locals())
                sentiment = result.iloc[0,0]

                level = ""
                if sentiment is not None:
                    sentiment = sentiment[2:]
                    count = result.iloc[0,1]
                    pct = round(count/num_sent*100,0)

                    if pct > 85:
                        level = "extremely"
                    elif pct > 70:
                        level = "very"
                    elif pct > 50:
                        level = "generally"
                    else:
                        level = "mildly"
                    # return bot's response
                    dispatcher.utter_message("Entity: {}".format(aspect))
                    dispatcher.utter_message("Intent: Get Sentiment")
                    dispatcher.utter_message("There are {} mentions associated with {}. They are {} {} (~{}%).".format(num_sent, aspect, level, sentiment, pct))
                # exception handling: initialise to neutral sentiment if not able to retrieve.
                else:
                    # return bot's response
                    dispatcher.utter_message("Entity: {}".format(aspect))
                    dispatcher.utter_message("Intent: Get Sentiment")
                    dispatcher.utter_message("I'm terribly sorry. It seems there's a technical issue: I'm unable to retrieve any sentiment somehow.")
            return []
        

class ActionGetEmotion(Action):

    def name(self) -> Text:
        return "action_respond_emotion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        aspect = tracker.get_slot("aspect_type")

        # return if aspect not found among valid list
        if aspect not in listOfAspects:
            # return bot's response
            dispatcher.utter_message("Entity: {}".format(aspect))
            dispatcher.utter_message("Intent: Get Emotion")
            dispatcher.utter_message("{} isn't a valid aspect I can handle.".format(aspect))
            return [FollowupAction("utter_suggest_aspect")]
        
        else:
            # read from BERT model output contained in csv file
            df = pd.read_csv(filename, delimiter = ',')

            # threshold score to pick out sentences related to that aspect
            threshold = 0.6

            # extract out sentences associated with specified aspect
            #sql = f"SELECT Emotion, {aspect} FROM df where {aspect} > {threshold}" # replaced
            sql = f"SELECT Emotion, Aspect FROM df where Aspect LIKE '%{aspect}%'" # newly ammended code
            
            subquery = ps.sqldf(sql, locals())
            subquery2 = ps.sqldf("SELECT Emotion, COUNT(Emotion) As count FROM subquery GROUP BY Emotion", locals())

            # get total number of sentences related to that aspect
            result = ps.sqldf("SELECT sum(count) as total FROM subquery2", locals())
            num_sent = result.iloc[0,0]

            # exception handling: initialise to zero count if no result retrieved in earlier step
            if num_sent is None:
                num_sent = 0
                # return bot's response
                dispatcher.utter_message("Entity: {}".format(aspect))
                dispatcher.utter_message("Intent: Get Emotion")
                dispatcher.utter_message("Unfortunately, it seems there isn't any notable mentions relating to {}.".format(aspect))
            else:       
                # get associated sentiment to that aspect
                result = ps.sqldf("SELECT Emotion, max(count) FROM subquery2", locals())
                emotion = result.iloc[0,0]

                if (emotion is not None) and (emotion.find("NIL") == -1):
                    emotion = emotion[2:]
                    count = result.iloc[0,1]
                    pct = round(count/num_sent*100,0)
                    # return bot's response
                    dispatcher.utter_message("Entity: {}".format(aspect))
                    dispatcher.utter_message("Intent: Get Emotion")
                    dispatcher.utter_message("With respect to {}, management sounded a general {}(~{}%) tone to it.".format(aspect, emotion, pct))   
                # exception handling: initialise to neutral sentiment if not able to be retrieved.
                else:
                    # return bot's response
                    dispatcher.utter_message("Entity: {}".format(aspect))
                    dispatcher.utter_message("Intent: Get Emotion")
                    dispatcher.utter_message("There is generally an apathetic tone with regards to {}.".format(aspect))
            return []
                
                
class ActionGetSentence(Action):

    def name(self) -> Text:
        return "action_respond_sentence"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        aspect = tracker.get_slot("aspect_type")
        
        # return if aspect not found among valid list
        if aspect not in listOfAspects:
            # return bot's response
            dispatcher.utter_message("Entity: {}".format(aspect))
            dispatcher.utter_message("Intent: Get Sentence")
            dispatcher.utter_message("{} isn't a valid aspect I can handle.".format(aspect))
            return [FollowupAction("utter_suggest_aspect")]
        
        else:
            # read from BERT model output contained in csv file
            df = pd.read_csv(filename, delimiter = ',')
            
            threshold = 0.6
            sentiment = tracker.get_slot("sent_polarity")
            if sentiment is not None:
                sentiment = sentiment.lower() # convert to lower case
            
            emotion = tracker.get_slot("emot_polarity")
            if emotion is not None:
                emotion = emotion.lower() # convert to lower case
            
            # extract out sentences associated with specified aspect
            #sql = f"SELECT text, Sentiment, Emotion, {aspect} FROM df where {aspect} > {threshold} ORDER BY {aspect} DESC" # replaced
            
            # newly added code
            sql = f"SELECT text, Sentiment, Emotion, Aspect, {aspect} FROM df where Aspect LIKE '%{aspect}%' ORDER BY {aspect} DESC"
            subquery = ps.sqldf(sql, locals())
            
            # return if query retrieves zero text relevant to the aspect
            if len(subquery) <= 0:
                dispatcher.utter_message("Entity: {}".format(aspect))
                dispatcher.utter_message("Intent: Get Sentence")
                dispatcher.utter_message("Unfortunately, it seems there isn't any notable mentions relating to {}.".format(aspect))

            else:
                # case switch on sentiment: query sentences with only the respective sentiment, else retrieve all sentences
                def switcherSent (args):
                    switcher = {
                        'positive': f"SELECT text, sentiment, emotion FROM subquery WHERE sentiment like '%{sentiment}%'",
                        'negative': f"SELECT text, sentiment, emotion FROM subquery WHERE sentiment like '%{sentiment}%'",
                        'neutral':  f"SELECT text, sentiment, emotion FROM subquery WHERE sentiment like '%{sentiment}%'"
                    }
                    return switcher.get(args,"SELECT text, sentiment, emotion FROM subquery")

                sql = switcherSent(sentiment)
                subquery2 = ps.sqldf(sql, locals())
                # randomly pick a sentence 
                randomRow = subquery2.sample()
                stmt = randomRow.iloc[0,0]
                emotion = randomRow.iloc[0,2][2:]
                
                if emotion == "NIL": 
                    dispatcher.utter_message("Entity: {}".format(aspect))
                    dispatcher.utter_message("Intent: Get Sentence")
                    dispatcher.utter_message("One notable mention with respect to {} is this:".format(aspect))
                    dispatcher.utter_message("\"{}\".".format(stmt))
                else:
                    dispatcher.utter_message("Entity: {}".format(aspect))
                    dispatcher.utter_message("Intent: Get Sentence")
                    dispatcher.utter_message("One notable mention with respect to {} is this:".format(aspect))
                    dispatcher.utter_message("\"{}\".".format(stmt))
                    dispatcher.utter_message("Management sounded {} on this statement".format(emotion))
            return []
    
    