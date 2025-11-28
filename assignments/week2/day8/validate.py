class NegativeAge(Exception):
    pass

class OverAge(Exception):
    pass


def get_name():
    name=input("Please enter your name: ")
    if not name.isalpha() :
        raise ValueError("Name should only include alphabet")
    return name

def get_age():
    age_input = input("Please enter your age: ")

    age = int(age_input)
    if age < 0:
        raise NegativeAge("age cannot be negative")
    if age>150:
        raise OverAge("Don't exists normally\n")
    return age

def get_favourite_number():
    number = input("Please enter your favourite number: ")
    return float(number)