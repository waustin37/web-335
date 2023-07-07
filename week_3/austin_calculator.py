#################################################
# Title: Exercise 3.3 - Python Variables and Functions
# Author: William Austin
# Date: June 10, 2023
# Description: Creating a Simple Calculator 
#################################################


#List of functions for simple arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


#variables to test each function
num1 = 3
num2 = 4
num3 = 5
num4 = 2

#variables for test results as well as print commands to show those results in the desired format
sum = add(num1, num2)
print (str(num1) + " + " + str(num2) + " is " + str(sum))
difference = subtract(num3, num4)
print (str(num3) + " - " + str(num4) + " is " + str(difference))
product = multiply(num1,num3 )
print (str(num1) + " * " + str(num3) + " is " + str(product))
quotient = divide(num2, num4)
print (str(num2) + " / " + str(num4) + " is " + str(quotient))


#Final output variable showing the results without showing the 'work'
output =  "Addition is " + str(sum) + "\nSubtraction is " + str(difference) + "\nMultiplication is " + str(product) + "\nDivision is " + str(quotient)

#Printing that output
print(output)





