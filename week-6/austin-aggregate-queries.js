/**
	Title: austin-aggregate-queries.js
    Author: William Austin
    Date: July 1, 2023
    Description: Aggregate Queries 
 */

//A query to show a list of documents in the houses collection
db.houses.find();

//A query to show a list of documents in the students collection
db.students.find();

//A query to add a new student to the students collection
db.students.insertOne(
    {"firstName":"William", 
    "lastName":"Austin", 
    "studentId":"s1019", 
    "houseId":"h1010"});

//A query to prove that document was added
db.students.findOne({studentId:"s1019"});

//A query to delete the recently added document
db.students.deleteOne({lastName:"Austin"})

//A query to show that William Austin is no longer in Syltherin House
db.students.find({houseId:'h1010'})

//A query to show a list of students by house
db.houses.aggregate([
    {
        $lookup:
        {
            from:"students",
            localField: "houseId",
            foreignField: "houseId",
            as: "Students"
        }
    }
])

//A query to show a list of Gryffindor Students
db.houses.aggregate([
    {
        $lookup:
        {
            from:"students",
            localField:"houseId",
            foreignField:"houseId",
            as: "Gryffindors"
        }
    },
    {
        $match:
        {"house.houseId": "h1007"}
    }
])


//A query to show a list of Ravenclaw Students by matching them to their mascot
db.houses.aggregate([
    {
        $lookup:
        {
            from:"students",
            localField:"houseId",
            foreignField:"houseId",
            as: "Eagles"
        }
    },
    {
        $match:
        {"mascot": "Eagle"}
    }
])