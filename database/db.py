import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

client = pymongo.MongoClient(os.getenv("MONGO_URI"))

db = client["FamilyTracker"]
family_collection = db["FamilyMembers"]

