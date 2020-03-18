## query sentiment
* greet
  - utter_greet
* query_sentiment{"aspect_type":"sales"}
  - action_respond_sentiment
* thanks
  - utter_can_i_help

## query sentiment + aspect
* greet
  - utter_greet
* query_sentiment
  - utter_ask_aspect
* inform{"aspect_type":"sales"}
  - action_respond_sentiment
* thanks
  - utter_can_i_help

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
