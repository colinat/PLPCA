## query sentiment + aspect: sales
* greet
  - utter_greet
* query_sentiment{"aspect_type":"sales"}
  - action_respond_sentiment
* thanks
  - utter_can_i_help
  
## query sentiment + aspect: earnings
* greet
  - utter_greet
* query_sentiment{"aspect_type":"earnings"}
  - action_respond_sentiment
* thanks
  - utter_can_i_help
  
## query sentiment + aspect: op_costs
* greet
  - utter_greet
* query_sentiment{"aspect_type":"op_costs"}
  - action_respond_sentiment
* thanks
  - utter_can_i_help
  
## query sentiment + aspect: products_services
* greet
  - utter_greet
* query_sentiment{"aspect_type":"products_services"}
  - action_respond_sentiment
* thanks
  - utter_can_i_help
  
## query sentiment + aspect: organic_expansion
* greet
  - utter_greet
* query_sentiment{"aspect_type":"organic_expansion"}
  - action_respond_sentiment
* thanks
  - utter_can_i_help

## query sentiment + aspect: acquisitions
* greet
  - utter_greet
* query_sentiment{"aspect_type":"acqusitions"}
  - action_respond_sentiment
* thanks
  - utter_can_i_help
  
## query sentiment + aspect: competition
* greet
  - utter_greet
* query_sentiment{"aspect_type":"competition"}
  - action_respond_sentiment
* thanks
  - utter_can_i_help
  
## query sentiment + aspect: op_risks
* greet
  - utter_greet
* query_sentiment{"aspect_type":"op_risks"}
  - action_respond_sentiment
* thanks
  - utter_can_i_help
  
## query sentiment + aspect: debt
* greet
  - utter_greet
* query_sentiment{"aspect_type":"debt"}
  - action_respond_sentiment
* thanks
  - utter_can_i_help


## query sentiment + no aspect
* greet
  - utter_greet
* query_sentiment
  - utter_suggest_aspect
* inform
  - action_respond_sentiment
* thanks
  - utter_can_i_help

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
