def welcome():
    print("welcone to the screen")

def eligibilty(name="student" , age=18):
    if age>=18:
        print(f"{name} you are eligible to vote")
    else:
        print(f"{name} you are not eligible to vote")

def square(side):
    area=side*side
    print(f"the area of a square is {area}")

def bmi_calculator(height,weight):
    bmi=weight/(height**2)
    return f"your bmi index is {bmi}"

mul = lambda x: x*x
