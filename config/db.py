from pymongo import MongoClient
from os import environ

MONGO_URI = environ["MONGODB_PASS"]

conn = MongoClient(MONGO_URI)