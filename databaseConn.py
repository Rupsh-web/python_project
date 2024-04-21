#importing necessary libraries. before that install pymongo to connect using mongo db pip install pymongo
import pymongo
from pymongo import MongoClient #The MongoClient() class for the PyMongo driver library for MongoDB creates client instances. Its main function is to enable you to connect to the MongoDB database

#connect to MongoDb database
host="localhost"  #default hostname or give hostname or ip addresss of mongodb servewr
port=27017 #default MongoDb port

# Create a MongoClient
client = MongoClient(host, port)
# Access a database
db = client["admin"]
collection = db["admin"]
# Get user input
name = input("Enter your full name: ")
emaill = input("Enter registered email id: ")
age = input("Enter the current age in year: ")
dob = input("Enter the date of birth (YYYY-MM-DD): ")
address= input("Enter permanent address: ")
roll=input("Enter roll no of applicant: ")
# Create a document
new_document = {
    "name": name,
    "email": emaill,
    "age": age,
    "dob":dob,
    "address":address,
    "roll":roll
}

# Insert the document into the collection
insert_result = collection.insert_one(new_document)

# Print the inserted document's ID
print("Inserted document ID:", new_document)
