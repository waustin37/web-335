#################################################
# Title: Exercise 6.3 - 
# Author: William Austin
# Date: July, 1 2023
# Description: 
#################################################

from pymongo import MongoClient

client = MongoClient('mongodb+srv://web335_user:s3cret@cluster0.hkbvlmn.mongodb.net/?retryWrites=true&w=majority')

db = client['web335DB']

print(client)

for user in db.users.find():
    print(user)


print(db.users.find_one({"employeeID":"1011"}))

print(db.users.find_one({"lastName":"Mozart"}))
