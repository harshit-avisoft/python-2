# 1
# with open("r1.txt") as f:
#     content=f.read()
#     print(content)

# 2
# with open("r1.txt","r") as f:
#     content1=f.readline()
#     content2=f.readline()
#     content3=f.readline()
#     print(content1,content2,content3)


# 3
# with open("r1.txt","w") as f:
#     f.write("hey\n")
#     f.write("How\n")
#     f.write("are\n")
#     f.write("you\n")
#     f.write("?\n")

# with open("r1.txt","r") as f:
#     content=f.read()
#     print(content)


# 4
# with open("r1.txt","a") as f:
#     f.write("I am good")

# with open("r1.txt","r") as f:
#     content=f.read()
#     print(content)


# 5
# with open("r2.txt","w") as f:
#     f.write("hey everyone")

# with open("r2.txt","r") as f:
#     content=f.read()
#     print(content)
# print(f.closed)

# 6
# with open("r1.txt","r") as f:
#     content=f.readlines()
#     for line in content:
#         if len(line)>20:
#             print(line)

# 7
# with open("r1.txt","r") as f:
#     content=f.read()
#     sum=0
#     for line in content:
#         if line!=" ":
#             sum+=int(line)
#     print(sum)


# 8
# with open("r1.txt","r+") as f:
#     content=f.read()
#     count=0
#     temp=""
#     while count<10:
#         temp+=content[count]
#         count+=1
#     print(temp)
#     f.write("python")


# 9
# with open("r1.txt","r") as f:
#     content1=f.read()
#     content2=f.readlines()
#     count=0
#     for line in content1:
#         if line!=" ":
#             count+=1
#     print(count)
#     print(len(content2))
    
# 10
# with open("r1.txt","r") as f:
#     content=f.read()

# with open("r2.txt","w") as f:
#     f.write(content)

