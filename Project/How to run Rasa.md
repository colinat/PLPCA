## setup
1. Create new conda environment with python 3.7
2. Activate conda environment created. Install rasa using pip => "pip install rasa"


## configuration (for brand new copy)
1. Go to project directory in anaconda prompt. Run "rasa init"
2. Edit config.yml, data/nlu.md and data/stories.md to configure intents, queries and bot responses. (Refer to https://rasa.com/docs/rasa/user-guide/building-assistants/ for tips) 

## training NLU classifier
1. Run "rasa train" in anaconda prompt to train NLU model.
2. Run another command window. Run "rasa run actions" to run the action listener.
3. In the base window, run "rasa shell" to run the chatbot.


## When problems is still encountered while running rasa
Install other require necessary packages using pip => "pip install google-auth==1.10.1 prompt-toolkit==2.0.10 questionary==1.4.0 SQLAlchemy==1.3.12 urllib3==1.25.7". This is to prevent error loop in rasa shell.
To test trained chatbot, run "rasa shell"

## To change the port number in rasa
	rasa run -m models --enable-api --cors “*” --debug -p 5005
	
## How to integrate rasa to webpage (webchat)
1st :-  Install react, below are the sequence:-
        1. npm install  webpack@^4.0.0 --save
		2. npm install react@16.13.1 --save
		3. npm install bufferutil@^4.0.1 --save
		4. npm install utf-8-validate@^5.0.2 --save
		5. Then finally, npm install rasa-webchat
		

After these installation follow the below steps:-
Step1: Once you have your bot ready and then we can connect the bot with the webchat

so add the below congfiguration in the credentials.yml file:
socketio:
  user_message_evt: user_uttered
  bot_message_evt: bot_uttered
  session_persistence: true
you can read more about this in the link below:

https://rasa.com/docs/rasa/user-guide...

Step2: Now  let us start our bot using the below command:

rasa run -m models --enable-api --cors "*" --debug

Step3: Now you can see different api details for our rasa bot server
 Now we can connect our bot to a webpage using the webchat script

https://github.com/mrbot-ai/rasa-webchat

now create a webpage and add the below code:

copy the code from the above link and paste it in the body tag

step4: Now change the socket url port number to our rasa server's port number

Step5: Now let's test our bot

Now you can see we got the response

		