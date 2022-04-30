from asyncore import dispatcher
from typing import Any, Text, Dict, List, Union


from rasa_sdk import Action, Tracker
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher

from urllib import response
import urllib.parse
import urllib.request
import webbrowser
import json
import ast

import sqlite3
path_to_db = "actions/store.db"

class ActionPPT(Action):
    def name(self) -> Text:
        return "action_ppt"
    
    async def run(
        self,
        despatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        webpage_url="https://sdpecommerceproject.wixsite.com/ecommerceplatform"
        webbrowser.open(webpage_url)
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


        



# python -m rasa run actions 