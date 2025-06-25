import os
import pymongo
from dotenv import load_dotenv

load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

client = pymongo.MongoClient(MONGO_DB_URL)

print("Listing databases and collections with document counts:")

for db_name in client.list_database_names():
    db = client[db_name]
    print(f"\nDatabase: {db_name}")
    for coll_name in db.list_collection_names():
        collection = db[coll_name]
        count = collection.count_documents({})
        print(f"  Collection: {coll_name} - Documents: {count}")
