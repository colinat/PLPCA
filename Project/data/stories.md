## greet
* greet
  - utter_greet

## startbot
* get_started
  - utter_greet

## query sentiment on sales
* query_sentiment{"aspect_type":"sales"}
  - action_respond_sentiment
* thanks
  - utter_can_i_help
  
## query sentiment on earnings
* query_sentiment{"aspect_type":"earnings"}
  - action_respond_sentiment
* thanks
  - utter_can_i_help

## query sentiment on op_costs
* query_sentiment{"aspect_type":"op_costs"}
  - action_respond_sentiment
* thanks
  - utter_can_i_help
  
## query sentiment on products_services
* query_sentiment{"aspect_type":"products_services"}
  - action_respond_sentiment
* thanks
  - utter_can_i_help
    
## query sentiment on organic_expansion
* query_sentiment{"aspect_type":"organic_expansion"}
  - action_respond_sentiment
* thanks
  - utter_can_i_help
  
## query sentiment on acquisitions
* query_sentiment{"aspect_type":"acquisitions"}
  - action_respond_sentiment
* thanks
  - utter_can_i_help

## query sentiment on competition
* query_sentiment{"aspect_type":"competition"}
  - action_respond_sentiment
* thanks
  - utter_can_i_help
  
## query sentiment on op_risks
* query_sentiment{"aspect_type":"op_risks"}
  - action_respond_sentiment
* thanks
  - utter_can_i_help

## query sentiment on debt
* query_sentiment{"aspect_type":"debt"}
  - action_respond_sentiment
* thanks
  - utter_can_i_help

## query sentiment
* query_sentiment
  - utter_suggest_aspect
* inform  
  - action_respond_sentiment
* thanks
  - utter_can_i_help


## ask_what_can_u_do
* ask_what_can_u_do
  - utter_help

## out_of_scope
* out_of_scope
  - utter_out_of_scope
   

## query sentence on sales
* query_sentence{"aspect_type":"sales"}
  - action_respond_sentence
* thanks
  - utter_can_i_help
  
## query sentence on earnings
* query_sentence{"aspect_type":"earnings"}
  - action_respond_sentence
* thanks
  - utter_can_i_help

## query sentence on op_costs
* query_sentence{"aspect_type":"op_costs"}
  - action_respond_sentence
* thanks
  - utter_can_i_help
  
## query sentence on products_services
* query_sentence{"aspect_type":"products_services"}
  - action_respond_sentence
* thanks
  - utter_can_i_help
    
## query sentence on organic_expansion
* query_sentence{"aspect_type":"organic_expansion"}
  - action_respond_sentence
* thanks
  - utter_can_i_help
  
## query sentence on acquisitions
* query_sentence{"aspect_type":"acquisitions"}
  - action_respond_sentence
* thanks
  - utter_can_i_help

## query sentence on competition
* query_sentence{"aspect_type":"competition"}
  - action_respond_sentence
* thanks
  - utter_can_i_help
  
## query sentence on op_risks
* query_sentence{"aspect_type":"op_risks"}
  - action_respond_sentence
* thanks
  - utter_can_i_help

## query sentence on debt
* query_sentence{"aspect_type":"debt"}
  - action_respond_sentence
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


## bot challenge
* bot_challenge
  - utter_iamabot
