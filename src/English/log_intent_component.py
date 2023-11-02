from typing import Dict, Text, Any, List

from rasa.engine.graph import GraphComponent, ExecutionContext
from rasa.engine.recipes.default_recipe import DefaultV1Recipe
from rasa.engine.storage.resource import Resource
from rasa.engine.storage.storage import ModelStorage
from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.training_data.training_data import TrainingData

from datetime import datetime
import pymysql

# DB connection details
MYSQL_HOST = "tracktechlk.com"
MYSQL_USER = "tracktec_inuka"
MYSQL_PASSWORD = "Kasuni.2000"
MYSQL_DATABASE = "tracktec_inuka1"

# Establish a connection to DB
db = pymysql.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)

# cursor = db.cursor()

def insert_data(table_name, d):
        insert_query = ""

        if table_name == "Product_Chats":
            insert_query = "INSERT INTO Product_Chats (MsgTime, Lang, Product_Type, Product, Intent) VALUES (%s, %s, %s, %s, %s)"
            
        elif table_name == "General_Chats":
            insert_query = "INSERT INTO General_Chats (MsgTime, Lang, Intent) VALUES (%s, %s, %s)"
            
        db.ping() #reconnecting mysql
        with db.cursor() as cursor:
            cursor.execute(insert_query, d)
        db.commit()
        print("Added data: ",d)


# TODO: Correctly register component with its type
@DefaultV1Recipe.register(
    [DefaultV1Recipe.ComponentType.INTENT_CLASSIFIER], is_trainable=True
)
class LogIntentsComponent(GraphComponent):
    @classmethod
    def create(
        cls,
        config: Dict[Text, Any],
        model_storage: ModelStorage,
        resource: Resource,
        execution_context: ExecutionContext,
    ) -> GraphComponent:
        # TODO: Implement this
        ...

    def train(self, training_data: TrainingData) -> Resource:
        # TODO: Implement this if your component requires training
        ...

    def process_training_data(self, training_data: TrainingData) -> TrainingData:
        # TODO: Implement this if your component augments the training data with
        #       tokens or message features which are used by other components
        #       during training.
        ...

        return training_data

    

    def process(self, messages: List[Message]) -> List[Message]:
        try:
            # Your existing code here
            print(messages[0].get_full_intent())
            intent = messages[0].get_full_intent()

            d = {}
            d['name'] = intent['name']
            d['confidence'] = intent['confidence']

            # Add the timestamp as a Date field to the dictionary
            timestamp = datetime.now()
            d['timestamp'] = timestamp

            #add language
            d['language'] = 'Eng'

            # CREATE TABLE Product_Chats(
            #     ID INT NOT NULL AUTO_INCREMENT,
            #     MsgTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            #     Lang VARCHAR(10) NOT NULL,
            #     Product_Type VARCHAR(20) NOT NULL,
            #     Product VARCHAR(30) NOT NULL,
            #     Intent VARCHAR(30) NOT NULL,v
            #     PRIMARY KEY (ID)
            # );

            if intent['name']=='faq':
                name = messages[0].as_dict()['response_selector']['faq']['response']['intent_response_key']

                
                specific = name.split('/')[1]
                d['product'],d['intent'] = specific.split('$')
                d['product_type']='savings'
                # Insert data into Product_Chats table
                table_name = "Product_Chats"
                data = (d['timestamp'], d['language'], d['product_type'], d['product'], d['intent'])
                insert_data(table_name, data)
                
            else:
                # Insert data into General_Chats table
                table_name = "General_Chats"
                d['intent']=d['name']
                data = (d['timestamp'], d['language'], d['intent'])
                insert_data(table_name, data)
                
            print(d)

            return messages
        except Exception as e:
            # Handle exceptions here, you can log the error message
            # and return an appropriate response or handle it in any other way.
            print(f"An error occurred: {str(e)}")
            # Optionally, you can raise the exception again to propagate it.
            # raise e
            return messages