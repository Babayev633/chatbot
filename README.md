# chatbot
chatbot for e-commerce website also connected to Telegram based on rasa. This project includes material about how correctly integrate sqlite to rasa and connect to http ports.

READ ME

Requirements:
Conda enviroment, for this project anaconda was used

Create an enviroment:
conda create --name myenv python 3.9 
This project were developed on python 3.9 as Rasa version is 3.1 and it supports it. Old versions of rasa will not support python 3.0 so you can manage it to 3.8

Check for any pip updates:
pip3 install -U pip

Install latest rasa version:
pip3 install rasa

Go to bot repository:
cd C:/Users/user/Desktop/chatbot

Create initial bot (just to have a look to base code)
rasa init

Train bot (if any changes have been done):
rasa train

Run the bot:
rasa shell     (Run and debug: rasa shell --debug)

run latest model with enabled api to endpoint (move --debug if you dont want it)
rasa run -m models --enable-api --cors "*" --debug

Run custom actions:
rasa run actions -vv

For Telegram integration I used hgrok
More information you can find on official rasa docs

Overview of the files
data/stories.yml - contains stories

data/nlu.yml - contains NLU training data

data/rules.yml - contains the rules upon which the bot responds to queries

actions/actions.py - contains custom action/api code

domain.yml - the domain file, including bot response templates

store.db - open with sqlitestudio

NOTE:
Project is not done yet.
Future work:
  - Work on ordering product
  - Fixing stories ( some stories and buttonds cause bugs )
  - Working on stable connection with port
  - Fixin connection to Whatsapp via Twilio
