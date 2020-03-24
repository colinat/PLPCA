## query sentiment with aspect
* greet
  - utter_greet
* query_sentiment{"aspect_type":"sales"}
  - action_respond_sentiment
* thanks
  - utter_can_i_help
  
## query sentence
* greet
  - utter_greet
* query_sentence
  - utter_suggest_aspect
* inform
  - action_respond_sentence
* thanks
  - utter_can_i_help

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
