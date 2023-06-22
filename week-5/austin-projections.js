/**
	Title: austin-projections.js
    Author: William Austin
    Date: June 22, 2023
    Description: Projection Queries 
 */

 /**
 * Adds a new Composer Document to our Users List
 */
    db.users.insertOne(
        {"firstName":"Bob", 
        "lastName":"Dylan", 
        "employeeId":"1013", 
        "email":"bdylan@gmail.com", 
        "dateCreated": new Date()}
        )
 /**
 * Updates the email value for the Mozart Composer Document
 */
    db.users.updateOne({"employeeId":"1009"}, {"$set":{"email":"mozart@me.com"}})

 /**
 * Displays all the documents in our users collection, but only shows the First Name, Last Name, and email. 
 */

    db.users.aggregate([{$project : {firstName: 1 , lastName: 1, _id:0, email:1}}])
