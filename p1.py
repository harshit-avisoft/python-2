# print("hi")
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)


# for x in "banana":
#     print(x)


# fruits=["apple","banana","pomegranate"]
# for x in fruits:
#     print(x)
#     if x=="pomegranate":
#       break

# for x in range(10):
#     print(x)


# for x in range(2,6):
#     print(x)

# for x in range(1,10,3):
#     print(x)

# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")


# for x in range(6):
#     if x==3: break
#     print(x)
# else:
#     print("finally reached")

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)

# for x in [0,1,2]:
#  pass



# python functions

# def greet():
#     print("hellow ")


# greet()


# temp1 = 77
# celsius1 = (temp1 - 32) * 5 / 9
# print(celsius1)

# def fahrenheit_to_celsius(fahrenheit):
#   return (fahrenheit - 32) * 5 / 9

# print(fahrenheit_to_celsius(77))
# print(fahrenheit_to_celsius(95))
# print(fahrenheit_to_celsius(50))


# def get_greeting():
#   return "Hello from a function"

# print(get_greeting())


# def my_function():
#   pass


# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")


# def my_function(name): # name is a parameter
#   print("Hello", name)

# my_function("Emil") # "Emil" is an argument



# def my_function(country = "Norway"):
#   print("I am from", country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")


# def my_function(animal, name):
#   print("I have a", animal)
#   print("My", animal + "'s name is", name)

# my_function(animal= "dog", name = "Buddy")

# the order doesn't matter
# def my_function(animal, name):
#   print("I have a", animal)
#   print("My", animal + "'s name is", name)

# my_function(name = "Buddy", animal = "dog")


# def my_function(person):
#   print("Name:", person["name"])
#   print("Age:", person["age"])

# my_person = {"name": "Emil", "age": 25}
# my_function(my_person)

# x = "awesome"
  
# print("Python is" , x)



# a=int(1.1)
# b=int("12")

# c=float(1.2)
# d=float("2.3")

# e=str(1)
# f=str(1.1)

# print(type(a),type(b),type(c),type(d),type(e),type(f))


# print('hello')
# print("hello")
# print("hi 'ravi'")
# print('hi "haridas"')


# a='hp'
# print(a)

# a="""hi 
# everyone 
# my name is 
# hp """
# print(a)

# a='''hi 
# everyone 
# my name is 
# hp '''
# print(a)

# a="hello everyone"
# print(a[3])
# x=a[11]
# print(x)


# a="hello everyone"
# for x in a:
#     print(x)


# a="hello everyone"
# print(len(a))


# a="hi hello everyone"
# print("he" in a)

# a="hello everyone"
# if "llo" in a:
#     print("yes present")

# a="hi hello everyone"
# print("abc" not in a)

# a="hi hello everyone"
# if "abc" not in a:
#     print("abc not present")


# python slicing
# a="hello everyone"
# print(a[2:6])
# print(a[:7])
# print(a[4:])
# print(a[-5:-2])
# print(a[-5:])


# a="        Harshit Pandey"
# print(a.upper())
# print(a.lower())
# print(a.strip())

# a="h p"
# print(a.replace(" ","k"))

# a="h k ,p,"
# print(a.split(","))

# a="hello"
# b="world"
# c=a+b
# print(c)
# print(a+b)
# print(a+ " " + b)


# Python - Format - Strings
# age=23
# txt=f"my age is {age}"
# print(txt)


# age=23.01
# txt=f"my age is {age:.1f}"
# print(txt)


# txt=f"random num is {6*5}"
# txt="random num is {6*5}"
# print(txt)


# print("hi \r sh")


# a="harshit"
# b="12-3"
# print(b.isalnum())


# print(5>6)
# print(5==5)

# print(bool("Hello"))
# print(bool(0))
# print(bool(15))

# x=15
# y=0
# z="hello"
# a=""
# print(bool(x),bool(y),bool(z))
# print(bool(a))


#  the walrus operator
# num=[1,2,3,4,5]
# count=len(num)
# if count>3:
#     print(f"List has {count} elements")

#     if(count :=len(num))>3:
#         print(f"List has {count} element")


# and operator
# x=5
# print(x<10 and x>3)


# identity operator
# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is z)
# print(x is y)
# print(x == y)
# Difference Between is and ==
# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal


# membership operator
# fruits=["apple","anar","banana"]
# print("banana" in fruits)
# txt="hello world"
# print("he" in txt)


# print("type 1 for addition ")
# print("type 2 for subtraction ")
# print("type 3 for multiplication ")
# print("type 4 for division ")

# operation=input("which operation you want to perform: ")

# num1=int(input("enter the first number: "))
# num2=int(input("enter the second number: "))

# if(operation=="1"):
#     print("the sum of {num1} and num2 is " , num1+num2)

# if(operation=="2"):
#     print("the sum of {num1} and num2 is " , num1-num2)    
   

# if(operation=="multiply"):
#     print("the sum of {num1} and num2 is " , num1*num2)    

# if(operation=="divide" and num2!=0):
#     print("the sum of {num1} and num2 is " , num1/num2) 
# else :
#      print("invalid input")


# creating a list
# x=['a','b','c']
# print(x)


# thislist=["apple","banana","cherry"]
# if "apple" in thislist:
#     print("Yes, 'apple' is in the fruits list")


# thislist=["apple","banana","cherry"]
# thislist[2:3]=["a","b"]
# print(thislist)


# append items
# thislist=["apple","banana","cherry"]
# thislist.append("orange")
# print(thislist)

# insert items
# thislist=["apple","banana","cherry"]
# thislist.insert(1,"orange")
# print(thislist)

# extend list
# thislist=["apple","banana","cherry"]
# tropical=["mango","pineapple","papaya"]
# thislist.extend(tropical)
# print(thislist)


# Remove Specified Item
# thislist=["apple","banana","cherry"]
# thislist.remove("banana")
# print(thislist)


# thislist=["apple","banana","cherry"]
# thislist.pop(1)
# print(thislist)
# thislist.pop() # removes the last item


# del thisList[0]
# del thislist # deletes the entire list


# thislist.clear()

# loops in list
# thislist=["apple","banana","cherry"]
# for x in thislist:
#     print(x)

# for i in range(len(thislist)):
#     print(thislist[i])

# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]


