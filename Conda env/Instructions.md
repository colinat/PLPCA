## Installation/Set up
-- Install prerequisite software (needed for chatbot)
Install Build Tools for Visual Studio 2019 in your computer. 
Weblink: https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16

-- Import conda environment from yml file
Open anaconda prompt terminal. 
Run the following command: conda env create -f environment_Grp12NLP.yml
Run "conda activate rasa"

-- Alternative setup approach (using requirements.txt)
Open anaconda prompt terminal.
Create a new conda environment by running the following command: conda create --n your_env_name
Run "conda activate your_env_name"
Run "pip install -r requirements.txt" 