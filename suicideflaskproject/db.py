#db configuration file with mongodb

from flask import Flask
from flask_pymongo import pymongo
import urllib
from app import app

CONNECTION_STRING="mongodb+srv://ashishsv028:"+ urllib.parse.quote("mydbpassword") \
                  +"@ashishcluster-efhjg.mongodb.net/test2?retryWrites=true&w=majority"

client=pymongo.MongoClient(CONNECTION_STRING)
db=client.get_database('users_db') #here give db name otherwise it creates new db
db1=client.get_database('chemicals_db')

user_collection=pymongo.collection.Collection(db,'users_db')
chemical_collection=pymongo.collection.Collection(db1,'chemicals_db')

