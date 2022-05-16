from asyncio.windows_events import NULL
from asyncore import dispatcher
from typing import Any, Text, Dict, List, Union


from rasa_sdk import Action, Tracker
from rasa_sdk.events import EventType, UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher

from urllib import response
import urllib.parse
import urllib.request
import webbrowser
import requests
import json
import ast
import pandas as pd

import sqlite3
path_to_db = "actions/store.db"

class Time(Action):
    def name(self) -> Text:
        return "action_time"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> Dict[Text, Any]:
        Curl_time_api = "http://worldtimeapi.org/api/timezone/Asia/Baku"
        

        response = requests.get(Curl_time_api)
        data = json.loads(response.text)

        try:   
            print(data)
            time = data['datetime']
        
            print(f"Exact time is: {time[11:19]}")
            text = f"Exact time is: {time[11:19]}"
            dispatcher.utter_message(text)  
        except IndexError:
            dispatcher.utter_message("Something went wrong with WorldTimeApi, please try again later")

        return[]

class ActionPPT(Action):
    def name(self) -> Text:
        return "action_ppt"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> Dict[Text, Any]:
        #use this command if connected to external server or user-id based system (as server runs locally, command will open tab in admin pc)
        #webbrowser.open(webpage_url)
        webpage_url="https://sdpecommerceproject.wixsite.com/ecommerceplatform"
        dispatcher.utter_template("utter_presentationppt", tracker, link = webpage_url)
        return[]


class ActionProductSearch(Action):

    def name(self) -> Text:
        return "action_searchpname"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> Dict[Text, Any]:

        connection = sqlite3.connect(path_to_db)
        cursor = connection.cursor()

        result = tracker.get_slot("pname")
        con = sqlite3.connect(path_to_db)
        cursor = con.cursor()
        
        cursor.execute('SELECT * FROM Products WHERE name=?', (result,))
        rows = cursor.fetchall()
        dispatcher.utter_message(text = 'Found these products: \n')
        for row in rows:
            id = row[0]
            name = row[1]
            category = row[2]
            price = row[3]
            amount = row[4]
            description = row[5]
            delivery_fee = row[6] 
            print(row)
            text1 = "\nID: " + str(id) + "\n  Name: " + str(name) + "\n  Category: " + str(category) + "\n  Price: " + str(price) + "₼\n  Amount: " + str(amount) + "\n  Description: " + str(description) + "\n  Delivery fee: " + str(delivery_fee) + "\n\n"

            dispatcher.utter_message(str(text1))
            dispatcher.utter_message(image= row[7])

        return[]

class ActionCategorySearch(Action):

    def name(self) -> Text:
        return "action_searchcategory"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> Dict[Text, Any]:

        connection = sqlite3.connect(path_to_db)
        cursor = connection.cursor()

        result = tracker.get_slot("category")
        con = sqlite3.connect(path_to_db)
        cursor = con.cursor()
        
        cursor.execute('SELECT * FROM Products WHERE category=?', (result,))
        rows = cursor.fetchall()
        dispatcher.utter_message(text = 'Found these products by category: ' + str(result) + '\n')
        for row in rows:
            id = row[0]
            name = row[1]
            category = row[2]
            price = row[3]
            amount = row[4]
            description = row[5]
            delivery_fee = row[6] 
            print(row)
            text1 = "\nID: " + str(id) + "\n  Name: " + str(name) + "\n  Category: " + str(category) + "\n  Price: " + str(price) + "₼\n  Amount: " + str(amount) + "\n  Description: " + str(description) + "\n  Delivery fee: " + str(delivery_fee) + "\n\n"

            dispatcher.utter_message(str(text1))
            dispatcher.utter_message(image= row[7])

        return[]


class SearchProductName(Action):
    def name(self) -> Text:
        return "action_searchapi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> Dict[Text, Any]:


        pname = tracker.get_slot("pname")
        api_address = "http://35.223.157.105:30006/api/product/search/"
        url = api_address + pname

        response = requests.get(url)
        data = json.loads(response.text)
        df = pd.DataFrame(data, columns = ['id', 'name','amount','cost','details','subcategoryId','storeId', 'photoUrl'])

        try:
            dispatcher.utter_message(text = 'Found these products: \n')
            for i in range(len(df)) :
                id = df.loc[i, "id"]
                name = df.loc[i, "name"]
                amount = df.loc[i, "amount"]
                cost = df.loc[i, "cost"]
                details = df.loc[i, "details"]
                subcategoryId = df.loc[i, "subcategoryId"]
                storeId = df.loc[i, "storeId"]
                photoUrl = df.loc[i, "photoUrl"]
        
                print(f"id: {id} \nname: {name}, \namount: {amount}, \ncost: {cost}₼, \ndetails: {details}, \nsubcategoryId: {subcategoryId}, \nstoreId: {storeId}, \nphotoUrl: {photoUrl} \n\n")
                text1 = f"id: {id} \nname: {name}, \namount: {amount}, \ncost: {cost}₼, \ndetails: {details}, \nsubcategoryId: {subcategoryId}, \nstoreId: {storeId}, \nphotoUrl: {photoUrl}"
                dispatcher.utter_message(text1)
        except IndexError:
            dispatcher.utter_message("Nothing found")

            

        return[]



# python -m rasa run actions 