# Functions:-
# A function is  a reusable block of code that performs a specific task.
# Functions  are a fundamental concept in python and allow ypu to break your code into smaller,mangeable pieces.


#There are three type of scopes in function:
# 1 - Local Scope
# 2 - Global Scope 
# 3 - Non - Local Scope

# LOCAL SCOPE :-
# example 1 -
def my_function():
    x= 10  # x is the LOCAL VARIABLE
    print(x)  #accessing the LOCAL VARIABLE

# GLOBAL SCOPE :-
# Example 1 -
x=10   # x is the GLOBAL VARIABLE
def my_function():
    print(x)   #acessing the GLOBAL VARIABLE
my_function()        