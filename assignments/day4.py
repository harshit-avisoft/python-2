import random
import math
import datetime

def welcome():
    print("welcone to the screen")

def eligibilty(name="student" , age=18):
    if age>=18:
        print(f"{name} you are eligible to vote")
    else:
        print(f"{name} you are not eligible to vote")

def square():
    num=int(input("Enter a number to square: "))
    area=num*num
    print(f"the area of a square is {area}")

def bmi_calculator(height,weight):
    bmi=weight/(height**2)
    return f"your bmi index is {bmi}"

def square_number():
    num=int(input("Enter a number to square: "))
    mul = lambda x:x*x
    result=mul(num)
    return result


def counter():
    c=random.randint(1,100)
    num=int(input("Enter a number: "))
    count=1
    while num!=c:
        if num>c:
            num=int(input("your number is smaller . TRy again: "))
        else:
            num=int(input("your number is smaller . TRy again: "))
        count+=1
    print(f"you took {count} attempts")


def random_name():
    quotes = []
    num=int(input("enter the number of names to be filled"))
    print(f"Enter {num} names:")
    for i in range(num):
        q = input(f"name {i+1}: ")
        quotes.append(q)

    selected = random.choice(quotes)
    return f"Randomly selected name: \"{selected}\""

def calculate_log():
    num=float(input("enter a number"))
    base=float(input("enter log base"))

    log=math.log(num,base)
    return f"log base of {base} of {num}= {log:.3f}"

def perfect_square():
    num = int(input("Enter a number to check: "))
    root = math.sqrt(num)
    if root.is_integer():
        print(f"{num} is a perfect square (√{num} = {int(root)})")
    else:
        print(f"{num} is NOT a perfect square (√{num} = {root:.2f})")


def show_time():
    now=datetime.now()
    formatted = now.strftime("%A, %d %B %Y | %I:%M:%S %p")
    return f"Current time is:\n{formatted}"