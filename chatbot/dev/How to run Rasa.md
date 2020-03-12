## setup
1. Create new conda environment with python 3.7
2. Activate conda environment created. Install rasa using pip => "pip install rasa"


## configuration
1. Go to project directory in anaconda prompt. Run "rasa init"
2. Edit config.yml, data/nlu.md and data/stories.md to configure intents, queries and bot responses. (Refer to https://rasa.com/docs/rasa/user-guide/building-assistants/ for tips) 

## training NLU classifier
1. Run "rasa train" in anaconda prompt to train NLU model.
2. Install other require necessary packages using pip => "pip install google-auth==1.10.1 prompt-toolkit==2.0.10 questionary==1.4.0 SQLAlchemy==1.3.12 urllib3==1.25.7". This is to prevent error loop in rasa shell.
3. To test trained chatbot, run "rasa shell"