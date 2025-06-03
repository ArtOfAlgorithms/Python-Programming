# Exercise:
# input - 1234
# output - one two three four
output = ""
phone_number = input("Enter no.: ")
numbers = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five"
}
for i in phone_number:
    output += numbers[i] + " "
print(output)
