# tuples are ordered and unchangeable and allow duplicates
# eval function
# thistuple = ("apple", "banana", "cherry")
# print(thistuple)
# print(len(thistuple))

# Tuple With One Item
# thistuple = ("apple",)

# tuples can be of any particular data types and also can be mixed

# tuple constructor
# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets

# print(thistuple[1])
# print(thistuple[-1])
# print(thistuple[2:5])
# print(thistuple[:4])
# print(thistuple[2:])
# print(thistuple[-4:-1])

# check if items exists
# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")

# how to change the values of a tuple
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# y.append("orange") # add some data
# y.remove("apple") # remove data
# x = tuple(y)

# add tuple to a tuple
# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# del thistuple # deletes the tuple completely

# unpacking a tuple
# fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits
# (green, yellow, *red) = fruits
# (green, *yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)

# loop through a tuple
# for x in thistuple:
#   print(x)

# for i in range(len(thistuple)):
#   print(thistuple[i])

# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1

# join tuples
# tuple1= ("a","b","c")
# tuple2= (1,2,3)
# tuple3= tuple1 + tuple3

# multiply tuples
# fruits= ("apple","banana","cherry")
# mytuple= fruits*2

# tuples method
# Return the number of times the value 5 appears in the tuple:
# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# x = thistuple.count(5)

# count returns the first ocurrence of an element
# thistuple = (1,3,7,8,5,4,6,8,5)
# x= thistuple.index(8)

# len, indexing , if y in tuple, del , unpacking , loops , + , count , index