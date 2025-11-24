# 1
# import csv

# with open("people.csv","w",newline="") as f:
#     content=csv.writer(f)
#     content.writerow(["Harshit" , 23])
#     content.writerow(["Harsh" , 22])
#     content.writerow(["Raj" , 24])
#     content.writerow(["Ravi" , 20])
#     content.writerow(["SP" , 19])

# with open("people.csv",newline="") as f:
#     content=csv.reader(f)
#     for row in content:
#         print(row)

# 2
# import csv
# with open("people.csv",newline="") as f:
#     content=csv.reader(f)
#     sum=0
#     for row in content:
#         sum+=1
#     print(sum)


# 3
# import csv
# with open("people.csv","r",newline="") as f:
#     content=csv.reader(f)
#     count=0
#     for line in content:
#         count+=1
#         if count==2:
#             print(line)
#             break
    
# 4
