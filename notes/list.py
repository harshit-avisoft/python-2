# list are ordered , changeable and allow duplicates

# allow duplicates
# thisList=["apple","banana","cherry","apple","cherry"]
# print(len(thisList))

# list items can be of any types even of mixed types

# thisList=list(("apple","banana","cherry"))
# print(thisList[1])
# print(thisList[-1])
# print(thisList[2:5])
# print(thisList[:4])
# print(thisList[2:])
# print(thisList[-4:-1])

# check if items exists

# if "apple" in thisList:
# print("Yes")

# change items
# thisList[1]="blackcurrant"

# change a range of items
# thisList[1:3]=["blackcurrent","watermelon"]

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
# thisList[1:2]=["blackcurrent","watermelon"]

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
# thislist[1:3] = ["watermelon"]

# insert 
# thisList=["apple","banana","cherry"]
# thisList.insert(2,"watermelon")

# append
# thisList.append("orange")

# to append elements from other list to current list we use extend function
# thisList.extend(tropical)

# thisList=["apple","banana","cherry"]
# thistuple=("kiwi","orange")
# thisList.extend(thistuple)

# thisList.remove("banana")
# If there are more than one item with the specified value, the remove() method removes the first occurrence:

# renove specified index with pop
# thisList.pop(1)

# remove random element
# thisList.pop()

# removes specified index
# del thisList[0]

# deletes thisList completely
# del thisList

# The list still remains, but it has no content.
# thisList.clear()

# Loop Through a List
# for x in thislist:
#   print(x)

# for i in range(len(thislist)):
#   print(thislist[i])

# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

# using list comprehension
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# newlist = [expression for item in iterable if condition == True]
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# newlist = [x for x in fruits]
# newlist = [x for x in range(10)]
# newlist = [x for x in range(10) if x < 5]
# newlist = [x.upper() for x in fruits]
# Set all values in the new list to 'hello':
# newlist = ['hello' for x in fruits]
# Return "orange" instead of "banana":
# newlist = [x if x != "banana" else "orange" for x in fruits]
# print(newlist)

# Sort List Alphanumerically
# thislist = ["orange", "mango", "kiwi","Orange", "pineapple", "banana"]
# thislist.sort()

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()

# sort descending
# thisList=["orange","mango","kiwi","pineapple","banana"]
# thisList.sort(reverse=True)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)

# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# case-insensitive sort function
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)

# thislist.reverse()

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()

# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist[:]

# join 2 lists
# list3 = list1 + list2

# for x in list2:
#   list1.append(x)

# list1.extend(list2)


# Return the number of times the value 5 appears in a list:
# thistuple = [1, 3, 7, 8, 7, 5, 4, 6, 8, 5]
# x = thistuple.count(5)

# len,indexing, if y in list , insert, append , extend ,remove ,pop, del , clear , loops , copy ,  + , count