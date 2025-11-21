# weight=int(input("enter your weight in kg : "))
# height=float(input("enter your height in m : "))

# bmi=weight/(height**2)
# print(f"your bmi index is : {bmi:.2f}")

import random
def random_name():
    quotes = []
    num=int(input("enter the number of names to be filled"))
    print(f"Enter {num} names:")
    for i in range(num):
        q = input(f"name {i+1}: ")
        quotes.append(q)

    selected = random.choice(quotes)
    return f"Randomly selected name: \"{selected}\""

