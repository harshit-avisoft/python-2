# set are ordered unchangeable and duplicates are not allowed

# thisSet= {"apple","banana","cherry"}
# print(thisSet)

# True and 1 is considered the same value:
# thisset = {"apple","banana","cherry",True,1,2}
# print(thisset)

# False and 0 is considered the same value:
# thisset = {"apple","banana","cherry",False,0,2}


# print(len(thisset))

# set can be of any data types even of mixed data-type
# set constructor
# thisset = set(("apple","banana","cherry"))

# for x in thisset:
#     print(x)

# thisset = {"apple", "banana", "cherry"}
# print("banana" in thisset)

# Once a set is created, you cannot change its items, but you can add new items.

# add items
# thisset.add("orange")

# add sets
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)

# add any iterable
# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
# thisset.update(mylist)

# remove item -- remove and discard will perform the function
# thisset.remove("banana")
# thisset.discard("banana")

# Remove a random item by using the pop() method:
# x=thisset.pop()
# print(x)

# thisset.clear()

# del will delete the set completely
# del thisset

# loops in set
# for x in thisset:
#     print(x)

# union
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# set3 = set1 + set2
# ste3 = set1 | set2

# join multiple sets
# myset = set1.union(set2, set3, set4)
# myset = set1 | set2 | set3 | set4

# join set and a tuple
# x = {"a", "b", "c"}
# y = (1, 2, 3)
# z = x.union(y)

# update
# x.update(y)

# intersection
# x.intersection(y)
# set3 = set1 & set2

# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
# set1.intersection_update(set2)

# The values True and 1 are considered the same value. The same goes for False and 0.

# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
# set3=set1.difference(set2)
# set3 = set1 - set2

# The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
# set1.difference_update(set2)

# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
# set3 = set1.symmetric_difference(set2)
# ^ will also give the same results
# set3 = set1 ^ set2

# The symmetric_difference_update() method will also keep all  the duplicates, but it will change the original set instead of returning a new set.
# set1.symmetric_difference_update(set2)

# frozenset
# Like sets, it contains unique, unordered, unchangeable elements.
# Unlike sets, elements cannot be added or removed from a frozenset.

# x = frozenset({"apple", "banana", "cherry"})
# print(x)

# Frozenset Methods
# Being immutable means you cannot add or remove elements. However, frozensets support all non-mutating operations of sets.

