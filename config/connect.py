from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError, ConfigurationError
import os
from dotenv import load_dotenv

"""
Load environment variables from the .env file.
This is useful for managing configuration settings such as database credentials.
"""
load_dotenv()

"""
Retrieve individual components from environment variables.
These variables are used to construct the MongoDB connection URI.
"""
USERNAME = os.getenv('MONGO_USERNAME')
PASSWORD = os.getenv('MONGO_PASSWORD')
DATABASE_NAME = os.getenv('DATABASE_NAME')

"""
Construct the MongoDB URI.
This URI includes the username, password, and database name necessary 
to connect to the MongoDB Atlas cluster.
"""
MONGO_URI = f"mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.ywnsq.mongodb.net/{DATABASE_NAME}?retryWrites=true&w=majority"

def get_db():
    """
    Connects to the MongoDB database and returns the database object.

    Returns:
        Database: A MongoDB database object.

    Raises:
        ServerSelectionTimeoutError: If the connection to the database fails.
        ConfigurationError: If there is a configuration issue with the database.
    """
    try:
        client = MongoClient(MONGO_URI)
        db = client[DATABASE_NAME]
        client.admin.command('ping')
        return db
    except ServerSelectionTimeoutError as sste:
        """
        Handles server selection timeout errors that may occur while attempting to connect 
        to the MongoDB server.
        """
        print(f"Server selection timeout error: {sste}")
        raise
    except ConfigurationError as conf_err:
        """
        Handles configuration errors that may arise from incorrect connection 
        settings or parameters.
        """
        print(f"Configuration error: {conf_err}")
        raise
    except Exception as e:
        """
        Catches any unexpected errors that occur during the connection process.
        """
        print(f"An unexpected error occurred: {e}")
        raise
