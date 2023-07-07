#################################################
# Title: Exercise 7.3 - 
# Author: William Austin
# Date: July, 7 2023
# Description: Exercise practicing usign Python with MongoDB
# Work Cited : WEB 335 Python Guide
#################################################


#This will import the Mongo Client
from pymongo import MongoClient
import datetime

#This will build a connection string to connect to
client = MongoClient('mongodb+srv://web335_user:s3cret@cluster0.hkbvlmn.mongodb.net/?retryWrites=true&w=majority')

db = client['web335DB']

#First Create a New User Object to Insert
gaga = {
    "firstName":"Stefani",
    "lastName":"Germanotta",
    "employeeId":"1014",
    "email":"ladygaga@joanna.com",
    "dateCreated": datetime.datetime.utcnow()
}

#Inserts that object into our database as a new document
gaga_user_id = db.users.insert_one(gaga).inserted_id
print(gaga_user_id)

#Displays the newly created document
print(db.users.find_one({"employeeId":"1014"}))

#Code to update the email of our new document 
db.users.update_one(
    {"employeeId":"1014"},
    {
        "$set": {
            "email": "MotherMonster@gaga.com"
        }
    }
)

#Displays the newly updated document
print(db.users.find_one({"employeeId":"1014"}))

#This deletes our newly created and updated document
result = db.users.delete_one({
    "employeeId":"1014"
})
print(result)

#Search for the deleted document to prove it's gone
print(db.users.find_one({"employeeId":"1014"}))