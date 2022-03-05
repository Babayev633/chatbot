# chatbot
chatbot for e-commerce website based on rasa.

READ ME

Run:
Go to C disk
cd C:/

Create an virtual environment in anaconda prompt using the command :
py -m venv ./venv

Activate your environment using the command :
.\venv\Scripts\activate

Check for any pip updates:
pip3 install -U pip

Install latest rasa version:
pip3 install rasa

Go to bot repository:
cd C:/Users/user/Desktop/chatbot

Train bot (if any changes have been done):
rasa train

Run the bot:
rasa shell     (Run and debug: rasa shell --debug)

Overview of the files
data/stories.yml - contains stories

data/nlu.yml - contains NLU training data

data/rules.yml - contains the rules upon which the bot responds to queries

actions/actions.py - contains custom action/api code

domain.yml - the domain file, including bot response templates

productexample.db - open with sqlitestudio
