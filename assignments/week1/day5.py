# # 1
# with open("employees.txt","a") as f:
#     f.write("Name,Department\n")
#     f.write("Harshit,IT\n")
#     f.write("Aman,Mechanical\n")
#     f.write("Raj,Civil\n")
#     f.write("Ravi,Electrical\n")
#     f.write("Chandan,Agriculture")

# with open("employees.txt","r") as f:
#     content1=f.read()
#     print(content1,"\n")
#     # content2=f.readline()
#     # print(content2,"\n")
#     # content3=f.readlines()
#     # print(content3)

# with open("employees.txt","a") as f:
#     f.write("\nAdarsh ,Civil")








# # 2
# import csv
# with open("emp.txt") as txt, open("employees.csv","w",newline="") as csvfile:
#     content=csv.writer(csvfile)
#     for line in txt:
#         content.writerow(line.strip().split(","))

# with open("employees.csv",newline="") as f:
#     content=csv.reader(f)
#     for row in content:
#         print(row)










# # 3
# import json
# import csv

# data_list=[]

# with open("employees.csv") as f:
#     reader=csv.DictReader(f)
#     for row in reader:
#         data_list.append(row)

# # convert to json format
# with open("emp.json","w") as f:
#     json.dump(data_list,f)

# # read the json file
# with open("emp.json","r") as f:
#     content=json.load(f)
# print(content)


# 4
with open("emp.txt","r") as f:
    lines=f.readlines()

data=[]
for line in lines[1:]:
    cont=line.strip().split(",")
    data.append(cont)

names={}
for name,dept,salary in data:
    names[name]=int(salary)

high_salary={}
for name,dept,salary in data:
    if int(salary) > 40000:
        high_salary[name] = int(salary)

print("Name and Salary: ", names)
print("Employess earming greater than 40000: " ,high_salary)
