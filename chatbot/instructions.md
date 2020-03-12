### Clone files from github
git clone https://github.com/mohdsanadzakirizvi/iplbot.git

### Install python 3.6 (Not higher)
conda create -n whatevername python=3.6

### Install dependences
Find requirements.txt amongst the files, run the following cmd:
pip install -r requirements.txt

### Install and link spacy
Run this in command prompt
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en

Note*: Add ! in front to run above commands in jupyter
Note: medium (md) size is recommended over the intent classification performance

### Training NLU classifier
Run this in command prompt:
python -m rasa_nlu.train -c nlu_config.yml --data data/nlu_data.md -o models --fixed_model_name nlu --project current --verbose

Note!!: if step fails due to "en" cannot be loaded in spacy, open C:\Users\XXX\Anaconda3\envs\chatbot\Lib\site-packages\rasa_nlu\utils\spacy_utils.py
Go to line 36 and edit to:
        "model": 'en_core_web_md',



### test it out (jupyter or python command)
>>> from rasa_nlu.model import Interpreter
>>> nlu_model = Interpreter.load('./models/current/nlu')
>>> nlu_model.parse('what is happening in the cricket world these days?')

### Generate story paths (or dialogue flows) in html  (**this step may not be necessary, I think)
python -m rasa_core.visualize -d domain.yml -s data/stories.md -o graph.html

### Train conversational model (based on story paths)
python -m rasa_core.train -d domain.yml -s data/stories.md -o models/current/dialogue -c policies.yml

### Run action server (for listening in on user's inputs)
Run a new terminal window. Run the following command
python -m rasa_core_sdk.endpoint --actions actions

### Start core server in another window (for user's inputs)
python -m rasa_core.run -d models/current/dialogue -u models/current/nlu --endpoints endpoints.yml







