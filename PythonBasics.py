# print("Hello World!")
# print("*"*10)

# shift+ctrl+m - list of errors
# pylint - to show errors
# shift+ctrl+p - command palette

# formatting a code - x = 2 ctrl+s

# Java code in python - use jython
# jython convert python soce to java byte code and executated by jvm

# student_count = 1000  # defining a variable
# print(student_count)

# STRINGS
# """ for multi-line codes
# paragraph = """Hi there,
# This Param
# Blah blah blah
# """

# BUILT-IN FUNCTIONS
# print(len(paragraph))
# print(paragraph[0])
# print(paragraph[-1])
# print(paragraph[0:3])  # return new string with first 3 characters

# ESC CHARACTER - \
# print("Name \"Param\"")  output - "Param"
# \\ for back slash; \n for new line

# FORMATTED STRINGS
# first = "Param"
# last = "Chheda"
# full = f"{first} {last}"
# print(full) output - Param Chheda

# FUNCTIONS
# course = "Python programming"
# print(course.upper())
# print(course.lower())
# print(course.title())
# removes spaces from extremes - lstrip, rstrip for individuals
# print(course.strip())
# print(course.find("pro"))
# print(course.replace("p", "j"))
# print("Pro" in course)
# print("swift" not in course)

# WORKING WITH NUMBERS
# x = 2 + 3j - complex numbers
# print(10 // 3) returns integer

# print(round(2.9))
# print(abs(-2.9))
# import math module for more math functions

# TYPE CONVERSION
# input is always a string
# x = input("x: ")
# y = int(x) + 1          # int(x), float(x), bool(x),str(x)
# print(f"{x}, y:{y}")

# CONDITIONAL STATEMENTS
# temperature = 35
# if temperature > 30:
#     print("It's warm")
# elif temperature >25:
#     print("It's nice")
#     print("Drink Water")
# else:
#     print("Its cold")
# print("Done")
# Can also be written as:
# message = "It's Warm" if temperature > 30 else "It's nice" (only of if-else not elif) (ternary)

# LOGICAL OPERATORS - and, or, not
# if 3 > 2 and 4 > 3:
#     print("True")
# else:
#     print("False")

# LOOPS
# for number in range(3): # or range(1, 4):
#     print("Attempt", number + 1 * ".")

# FOR-ELSE
# successful = True
# for number in range(1, 4):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times but unsuccessful")

# primitive types - int, float, bool, string
# complex type - range

# WHILE
# number = 100
# while number > 0:
#     print(number)
#     number //= 2

# EXERCISE - Print
# 2
# 4
# 6
# 8
# We have 4 even numbers

# count = 0
# for i in range(1, 10):
#     if (i % 2 == 0):
#         print(i)
#         count += 1
# print(f"We have {count} even numbers")

# FUNCTIONS
# start with def
# name should be lowercase good practice
# def greet(first_name, last_name):
#     print(f"Hello {first_name} {last_name}")
#     print("Welcome")


# greet("Param", "Chheda")

# DEFAULT ARGUMENT FOR FUNCTION

# def increment(number, by=1):
#     return number + by


# print(increment(2, 5))

# VARIABLE NUMBER OF ARGUMENTS
# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     print(total)


# multiply(1, 2, 3, 4)
