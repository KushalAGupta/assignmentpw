#1 Explain the key features of Python that make it a popular choice for programming.
'''
Ans: The key features of the python programming language which makes it a popular choice are:
i.)Widely used in the industry : Python dominates the industry in the data science field and all the fields which have the data related problems because it have many inbuild packages for that.
ii.)Have lot of libraries for the data automation.
iii.) Have all the frameworks of frondend, backend and data analysis.
iv.) Helps in image and video processing.
v.) Have the libraries which really ease the database handling
'''
#Describe the role of predefined keywords in Python and provide examples of how they are used in a program
'''
Ans: Keywords are the predefined words that holds a specific meaning and have a specific purpose.
In python predefined keywords are the words that are already reserved by the python for it's syntax and hold the specific purpose and meaning.
These keywords cannot be used for by the programmer for defining the varibale names and function names.
Some keywords are for,while,if,else.

Examples of how keywords are used:
Program to check if number is odd or even
a = 10
if (a%2==0):
    print("Number is even")
else
    print("Number is odd")
 In the above program if and else keywords are used

Program to print 1 to 10 numbers using for keyword:
for i in range(1,11):
    print(i)
'''
#Compare and contrast mutable and immutable objects in Python with examples.
'''
Ans: Mutable objects are the objects which can be changed or are editable after the creation.
Mutable objects are helpful in data structure.
Mutable objects are used when we need to constantly change the information.

Example:List is the data structure which is mutable in nature.

Immutable objects are the objects in which we cannot change or edit after the creation.
Immutable objects can be used for fixed values.
Immutable objects are used for stroing the information which does not need change.

Example: Tuple and string are the immutable in nature.
'''

#Discuss the different types of operators in Python and provide examples of how they are used
'''
Ans: Operators are the special keywords / symbols that are used to perform operations on value or value.

Types of operators are : 
i.)Arithematic operator: These are used to perform the arithematic operations between the two objects.
operators are +,-,*,/,%
Ex: a + b
ii.)Comparison operator: Compares two value and return a boolean value.
operator are ==,!=,>,<,>=,<=
Ex : if a > b:
    print("A is bigger")
else
    print("B is bigger")
iii.)Logical operator: To perform the logical operations between two data. Used to when we need to see if either one conditon is fullfiel or both conditons according to needs.
Operators are and, or
Example:
while a > 10 and b > 5:
    print("1")       
    This program will stop running if either one of two conditons fails
iv.) Assignmennt operators : The operators which are used to assigning any values.
operators are: =,+=,-+,*=,/=
Example: a = 10
v.) Membership operators : It helps us in checking if the particualr character is present in the string or not
operators are in, not in
Example: a = "Pwskills"
print(p in a)
vi.) Identity operator : Compares location of 2 object or variable in memeory
operators are: is,is not
Example: a = 3
b = 6
print( a is b)
o/p: False
vii.) Bitwise operator : Every single thing in the computer gets operated on bit level and bitwise operators operate on bits manipulating indivisuals bits within integers.
operators are &,|,~,^,<<,>>
Example: 
print( 10 & 10)
o/p: 10
'''

#Explain the concept of type casting in Python with examples
'''
Ans: The process of changing the data type of a value or object. Its is necessary because while executing or computation using operators, there can be mismatch between the data.
Example: a = int (input("Enter the number: "))
As input() take input in the form of string  int() is used to convert that value to integer to perfor the approriate operations.
'''

#How do conditional statements work in Python? Illustrate with examples.
'''
Ans: The conditional statements helps you to code decisions based on some conditions which are required for the proper and smooth functioning of the programs.
Conditionals statements are if,if-else,if-elif-else,nested if-else.

Example: 
if condtion is True:
    this code block will execute 
elif condition is True:
    This code block will execute if the if block is not executed
else
    This will execute if neither is executed
'''

#Describe the different types of loops in Python and their use cases with examples.
'''
Ans: Loop statements help you to execute a block of code repeated times.
types of loops are 
i.)for loop
ii.)while loop

i.)for loop: It iterates over a sequence of elements.It have 2 blocks for and else block . else block only runs if the for block is executed completed without any break statement.
Syntax: 
for i in "pwskills":
    print(i)
else:
    print("Loop executed")
Usecase : It is used when we traverse through the finite collections

ii.)while loop: It repeatedly executes a block of code until a conditon is met. It have 2 blocks while and else block . else block only runs if the for block is executed completed without any break statement.
Syntax:
while i < n:
    print(i)
    i+1
else:
    print("Loop executed")
Usecase: It is used when we dont know how many number of times the repeatation is required
'''