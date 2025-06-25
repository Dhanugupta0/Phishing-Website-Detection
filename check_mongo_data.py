import os
import pymongo
from dotenv import load_dotenv

load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

client = pymongo.MongoClient(MONGO_DB_URL)
db = client["sample_mflix"]
collection = db["NetworkData"]

count = collection.count_documents({})
print(f"Number of documents in 'NetworkData' collection: {count}")

doc = collection.find_one()
print("Sample document:", doc)
