#################################################
# Title: Exercise 6.3 - 
# Author: William Austin
# Date: July, 1 2023
# Description: Python and Mongo Exercise 
#################################################


'''import the Mongo Client'''
from pymongo import MongoClient

client = MongoClient('mongodb+srv://web335_user:s3cret@cluster0.hkbvlmn.mongodb.net/?retryWrites=true&w=majority')

db = client['web335DB']


#Display a list of all the user documents
for user in db.users.find():
    print(user)

#Display the user with the following employee ID
print(db.users.find_one({"employeeId":"1011"}))

#Display the user with the following last name
print(db.users.find_one({"lastName":"Mozart"}))
