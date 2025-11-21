# q1
# fruits=["Mango","apple","orange","anaar","guava"]
# print(fruits[0],fruits[len(fruits)-1])

# q2
# l=[10,20,30]
# l.append(40)
# l.insert(1,15)
# l.remove(30)
# print(l)

# q3
# numbers=[1,2,3,4,5,6,7,8]
# print(numbers[0:4])
# print(numbers[-2:])
# print(numbers[2:6])


# q4
# names=["Alice","Bob","Charlie","David"]

# if "Charlie" in names:
#     print("yes")

# q5
# num=[1,2,3,4,5]

# i=0
# for i in range(len(num)):
#     print(num[i]*2)

# q6
# colors=["red","blue","green"]
# ind=colors.index('blue')
# colors.pop(ind)

# q7
# letter=["a","b","a","c","a","b"]
# i=0
# count=0
# for i in range(len(letter)):
#    if letter[i]=='a':
#       count+=1
# print(count)      


# q8
# items=[12,45,67,89,23]
# print(len(items))

# q9
# nums=[5,1,8,3,2]
# nums.sort()
# print(nums)

# q10
# marks=[88,92,75,63,98]
# print(max(marks))
# print(min(marks))

# q11
# a = [1, 2, 3]
# b = [4, 5, 6]

# c=a+b
# a=a+b
# a.extend(b)

# print(a)


#q12
# data=[1,2,3,44,44,5,5,3,7,8]
# new_data=list(set(data))

# new_data=[]
# for num in data:
#     if num not in new_data:
#         new_data.append(num)

# print(new_data)        


# q13
# nums=[10,20,30,40]
# nums.sort(reverse=True)
# print(nums)



# q14
# nums=[]
# if len(nums)==0:
#     print("length is 0")


# q15
# values = [1, 2, 3, 4, 5]
# print(sum(values))

# q16
# nums = [1, 2, 3, 4, 5, 6]
# nums1=[]
# for x in nums:
#   if x%2==0:
#     nums1.append(x**2)
# print(nums1)

# q17


# q18
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]

# ans=[]
# for x in a:
#     if x in b:
#       ans.append(x)
# print(ans)


# q19
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]

# ans=[]
# for x not in a:
#     if x in b:
#       ans.append(x)
# print(ans)

# tuple notes

# thistuple=("apple","banana","cherry")
# y=("orange",)
# thistuple+=y
# print(thistuple)

