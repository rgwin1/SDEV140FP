"""
db.py

handles MongoDB connection and provides database and collection objects for Family Tracker app.
"""

import pymongo
import os
from dotenv import load_dotenv

load_dotenv() #load environment variables from .env file

#mongodb client connection using uri from environment variable
client = pymongo.MongoClient(os.getenv("MONGO_URI"))

#select FamilyTracker database
db = client["FamilyTracker"]

#access FamilyMembers collection from FamilyTracker database
family_collection = db["FamilyMembers"]