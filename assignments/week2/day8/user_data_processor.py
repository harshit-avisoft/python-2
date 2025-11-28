# Custom Exception
class negativeage(Exception):
    pass

class overage(Exception):
    pass



def main():
 age=None
 favourite_number=None
 name=None
 result=None


 print("\n===================Menu===================\n")
 # name
 try:
    name=input("Please enter your name: ")
    if not name.isalpha() :
        raise ValueError("Name should only include alphabet")
 except ValueError as e:
    print("Invalid name✘: ",e,"\n")
    name=None


 # age
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


 # favourite number
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


 # result
 try:
    result=(100/favourite_number)
 except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
    result = None
 except TypeError:
    print("Can't divide 100 by your favourite number\n")
 except OverflowError:
    print("overflow ")
 except ValueError as e:
    print(e)


 # file operation
 file_name=input("Enter a file name: ").lower()
 content=None
 try:
    with open(file_name,"r") as f:
        content=f.read()
        print("\n-----File contents-----")
        print(content)

 except FileNotFoundError:
    print("No such File found\n")
 except PermissionError:
    print("You are not allowed to open that file: ")
 except Exception as e:
    print(e)
 finally:
    print("\nfile operation done: \n\n")



 print("=======================================================\n")
 if name is not None:
  print(f"{'Name':20}: {name}")
 if age is not None:
  print(f"{'Age':20}: {age}")
 if favourite_number is not None:
  print(f"{'favourite_number':20}: {favourite_number}")
 if result is not None:
  print(f"{'division result':20}: {result}")
 if content is not None:
  print(f"{'content of  file':20} :{content}\n")
 if age is None and name is None and favourite_number is None and content is None and result is None:
    print("                No data available")
 print("=======================================================")



# Call main
if __name__ == "__main__":
    main()