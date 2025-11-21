print("type 1 for addition")
print("type 2 for subtraction")
print("type 3 for multiplication")
print("type 4 for division")

operation = input("which operation you want to perform: ")
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

if operation == "1":
    print("the sum of", num1, "and", num2, "is", num1 + num2)

if operation == "2":
    print("the sum of", num1, "and", num2, "is", num1 - num2)

if operation == "3":
    print("the sum of", num1, "and", num2, "is", num1 * num2)

if operation == "4" and num2 != 0:
    print("the sum of", num1, "and", num2, "is", num1 / num2)
else:
    print("invalid input")
