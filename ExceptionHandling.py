# Exception Handling - ValueError, TypeError, ZeroDivisionError

try:
    age = int(input("Enter Age: "))
    print(age)
except TypeError:
    print("Invalid Value")
