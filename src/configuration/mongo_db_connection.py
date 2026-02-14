import os
import sys
import pymongo
import certifi

from src.exception import MyException
from src.logger import logging
from src.constants import DATABASE_NAME, MONGODB_URL_KEY

# loading the certificate authority to avoid timeout errors when connecting to MongoDB
ca = certifi.where()

class MongoDBClient:
    """
    MongoDBClient is responsible for establishing a connection to the MongoDB database
    Attributes:
        1. client: MongoClient ---> a shared MongoClient instance for the class
        2. databse: Database ---> the specific database the MongoClient connects to 
    Methods:
        1. __init__(databse_name: str) -> None:
            Initializes the MongoDB connection using the given databse name
    """
    client = None # ----------> shared MongoCLient instance across all MongoDBClient instances

    def __init__(self, database_name: str) -> None:
        """
        Initializes the connection to the MongoDB database.
        If no existing connection is found, it establishes a new one
        
        :param databaase_name: str --->
            Name of the MongoB database to connect to.
            default id set by DATABSE_NAME constant 
        :raises:
            MyException: 
                if there is an issue connecting wto the MongoDB or if the environment variable for the MongoDB URL is not set
        """
        try:
            # check if the MongoDB client connection is esstablished already.
            # if not established, create a new one
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment Variable '{MONGODB_URL_KEY}' is not set")
                
                # esatablish a new MongoDB client connection:
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection Successful")

        except Exception as e:
            raise MyException(e, sys)
        



        