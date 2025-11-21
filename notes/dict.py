# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(thisdict["brand"])
# print(len(thisdict))

# The values in dictionary items can be of any data type:

# thisdict= dict(name = "John" , age =36 , country ="Norway")

# access different items
# x = thisdict["model"]
# x = thisdict.get("model")

# keys will return list of keys
# x = thisDict.keys()

# add a new item
# car["color"] = "white"

# values will return list of values
# x = thisDict.values()

#  x = thisDict.keys()

# Check if Key Exists
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")

# change values
# thisdict["year"]=2018

# update dictionary
# thisdict.update({"year": 2020})

# adding new item
# thisdict["color"] = "red"

# remove items
# thisdict.pop("model")

# The popitem() method removes the last inserted item
# thisdict.popitem()

# The del keyword removes the item with the specified key name:
# del thisdict["model"]

# The del keyword can also delete the dictionary completely:
# del thisdict

# The clear() method empties the dictionary:
# thisdict.clear()

# loop for printing keys
# for x in thisdict:
    # print(x)

# loop for printing values
# for x in thisdict:
    # print(thisdict[x])

# for x in thisdict.values():
#   print(x)

# for x, y in thisdict.items():
#   print(x, y)

# copy a dictionary
# mydict = thisdict.copy()
# mydict = dict(thisdict)

# nested dictionary
# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3

# Print the name of child 2:
# print(myfamily["child2"]["name"])

# Loop Through Nested Dictionaries
# for x, obj in myfamily.items():
#   print(x)

#   for y in obj:
#     print(y + ':', obj[y])

