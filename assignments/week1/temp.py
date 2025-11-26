import day4
from day4 import counter
from day4 import random_name
from day4 import calculate_log as cal_log
from day4 import show_time
from day4 import perfect_square as p_s
from day4 import square_number as sn
from day4 import welcome
import math
import random
from datetime import datetime
from datetime import date



# math
p_s()

print(cal_log())
# random 
counter()
print(random_name())


# datetime
print(show_time())

d=date(2019,1,1)
print("modifide date:", d)



welcome()
day4.eligibilty("Harshit",25)
day4.square()
print(day4.bmi_calculator(1.70,55))
print(day4.mul(1))
print(sn())

# global 
name="harshit"
print(name)

def change():
    global name
    name="hp"
    return name

print(change())
