/**
	Title: austin-assignment-mongoDB-shell.js
    Author: William Austin
    Date: June 17, 2023
    Description: MongoDB Shell Queries 
 */


/**
 * Show the full list of users in our 'users' database
 */
db.users.find()

/**
 * Find the user with the email 'jbach@me.com'
 */
db.users.find({email : 'jbach@me.com'})

/**
 * Find the user with the last name 'Mozart'
 */
db.users.find({lastName:'Mozart'})

/**
 * Find the user with the first name 'Richard'
 */
db.users.find({firstName:'Richard'})

/**
 * Find the user with the employee ID '1010'
 */
db.users.find({employeeId:'1010'})
