## greet
* greet
  - utter_greet

## query sentiment with aspect
* query_sentiment{"aspect_type":"sales"}
  - action_respond_sentiment
* thanks
  - utter_can_i_help
  
## query sentence
* query_sentence
  - utter_suggest_aspect
* inform
  - action_respond_sentence
* thanks
  - utter_can_i_help

## say goodbye
* goodbye
  - utter_goodbye

## out_of_scope
* out_of_scope
  - utter_out_of_scope

## ask_what_can_u_do
* ask_what_can_u_do
  - utter_help

## bot challenge
* bot_challenge
  - utter_iamabot
