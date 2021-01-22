import pymongo
from pymongo import *

# Name of database
DatabaseName = "JobListDataBase"
# Collection list
collections = ["Accounts"]

def scrubDB(client):
    confirm = input("Are you sure you'd like to scrub this db [y/n]")
    if confirm == 'y':
        client.drop_database(DatabaseName)
        if verifyDBWasDropped(client):
            setupFreshDB(client)
            if not verifyDBWasDropped(client):
                return True
            return False
    return False

def verifyDBWasDropped(client: MongoClient):
    listDB = client.database_names()
    return DatabaseName not in listDB

def setupFreshDB(client: MongoClient):
    jlDB = client[DatabaseName]
    for coll in collections:
        tempPost = {"Default": "Data"}
        jlDB[coll].insert_one(tempPost)

dbClient = pymongo.MongoClient()

op = input("Please select operation [scrub]")
if op == "scrub":
    print(scrubDB(dbClient))
