# 1
with open("employees.txt","a") as f:
    f.write("Name,Department\n")
    f.write("Harshit,IT\n")
    f.write("Aman,Mechanical\n")
    f.write("Raj,Civil\n")
    f.write("Ravi,Electrical\n")
    f.write("Chandan,Agriculture")

with open("employees.txt","r") as f:
    content1=f.read()
    content2=f.readline()
    content3=f.readlines()
    print(content1,"\n")
    print(content2,"\n")
    print(content3)

with open("employees.txt","a") as f:
    f.write("\nAdarsh ,Civil")


# 2
import csv
with open("emp.txt") as txt, open("employees.csv","w",newline="") as csvfile:
    content=csv.writer(csvfile)
    for line in txt:
        content.writerow(line.strip().split(","))

with open("employees.csv",newline="") as f:
    content=csv.reader(f)
    for row in content:
        print(row)

# 3
import json
import csv
csv_file="employees.csv"
json_file="emp.json"

data_list=[]

with open(csv_file,encoding="utf-8") as f:
    reader=csv.DictReader(f)
    for row in reader:
        data_list.append(row)

with open(json_file,"w",encoding="utf-8") as f:
    json.dump(data_list,f,indent=4)



# 4
with open("emp.txt","r") as f:
    lines=f.readlines()

data=[line.strip().split(",") for line in lines[1:]]

name_salary={name: int(salary) for name, dept , salary in data}

high_earners= {name: int(salary) for name , dept , salary in data if int(salary)>40000}

print("Name: ", name_salary)
print("Employess earming greater than 40000: " ,high_earners)