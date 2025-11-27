class negativeage(Exception):
    pass

class overage(Exception):
    pass

age=None
favourite_number=None
name=None
result=None


print("\n===================Menu===================\n")
try:
    name=input("Please enter your name: ")
    if not name.isalpha() :
        raise ValueError("")
except ValueError as e:
    print("Invalid name✘: entered by the user",e,"\n")
    name=None

try:
    age_input = input("Please enter your age: ")

    age = int(age_input)
    if age < 0:
        raise negativeage("age cannot be negative")
    if age>150:
        raise overage("Don't exists normally\n")
except negativeage as e:
    print("Invalid age✘:",e)
except overage as e:
    print("Invalid age✘:",e)
except ValueError:
    print("Invalid age✘: Age must be integer\n")



try:
    favourite_number=input("Please enter your favourite number: ")
    favourite_number=float(favourite_number)
except TypeError:
    print("Number must be valid!!")
except OverflowError:
    print("Overflow error: number is too large to process")
except ValueError as e:
    favourite_number=None
    print("Invalid number✘ entered ")

try:
    result=(100/favourite_number)
except TypeError:
    print("Can't divide 100 by your favourite number\n")
except OverflowError:
    print("overflow ")
except ValueError as e:
    print(e)


file_name=input("Enter a file name: ").lower()

try:
    with open(file_name,"r") as f:
        content=f.read()
        print("\n-----File contents-----")
        print(content)

except FileNotFoundError:
    print("File not found\n")
except PermissionError:
    print("You are not allowed to open that file: ")
except Exception as e:
    print(e)
finally:
    print("\nfile closed now: \n\n")

print("=======================================================\n")
if name is not None:
 print(f"{'Name':20}: {name}")
if age is not None:
 print(f"{'Age':20}: {age}")
if favourite_number is not None:
 print(f"{'favourite_number':20}: {favourite_number}")
if result is not None:
 print(f"{'division result':20}: {result}")
print(f"{'content of  file':20} :{content}\n")
print("=======================================================")