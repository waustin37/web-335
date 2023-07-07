#################################################
# Title: Exercise 5.3 - Python Conditionals, Lists and Loops
# Author: William Austin
# Date: June 22, 2023
# Description: A Python exercise using new knowledge of conditionals, lists, and loops
#################################################


# Creating variables for array of Hobbies and Days of the Week
hobbies = ["Video Games", "Cooking", "Baking", "Weight Lifting", "Acting"]
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#Iterates over the hobbies and prints them to the console
for x in hobbies:
    print(x)


#Iterates over the days and prints a message depending on whether or not it's the weekend
for day in days:
    if day == "Saturday" or day =="Sunday":
        print("You're off today! Enjoy your hobbies!")
    else:
        print("GET TO WORK!!")