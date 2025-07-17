from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from typing import Generator
from pymongo.database import Database
from fastapi import Depends

USER_NAME = "root"
PASSWORD = "LubLnJmqEPrmFTmV"
HOST = "atlascluster.6jj4jw4.mongodb.net"

MONGO_URI = f"mongodb+srv://{USER_NAME}:{PASSWORD}@{HOST}/?retryWrites=true&w=majority&appName=AtlasCluster"
DB_NAME = "MBA"


def get_sync_mongo_db() -> Generator[Database, None, None]:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME] # Replace with your database name
    try:
        yield db
    finally:
        client.close()

# Define a type hint for easier use in route handlers
SyncMongoDep = Depends(get_sync_mongo_db)