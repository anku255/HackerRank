"""Complete the code in the editor below. The variables , , and  are already declared and initialized for you. You must:

Declare 3 variables: one of type int, one of type double, and one of type String.
Read 3 lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your 3 variables.
Use the + operator to perform the following operations: 
Print the sum of i plus your int variable on a new line.
Print the sum of d plus your double variable to a scale of one decimal place on a new line.
Concatenate s with the string you read as input and print the result on a new line."""

i = 12
d = 4.0
s = "HackerRank"

#Declaring variable and taking input for them
integer_var = int(raw_input())
double_var = float(raw_input()) #double in python is same as float
string_var = raw_input()

#Printing the final result
print i+integer_var
print d+double_var
print s+string_var
