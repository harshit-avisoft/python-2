# 1
# with open("employees.txt","r") as f:
#     content1=f.read()
#     content2=f.readline()
#     content3=f.readlines()
#     print(content1)
#     print(content2)
#     print(content3)

# with open("employees.txt","a") as f:
#     f.write("\nAdarsh ,Civil")


# 2
import csv
with open("emp.txt") as txt, open("data.csv","w",newline="") as csvfile:
    content=csv.writer(csvfile)
    for line in txt:
        content.writerow(line.strip().split(","))

with open("data.csv",newline="") as f:
    content=csv.reader(f)
    for row in content:
        print(row)

# 3
import json
csv_file="data.csv"
json_file="emp.json"

data_list=[]

with open(csv_file,encoding="utf-8") as f:
    reader=csv.DictReader(f)
    for row in reader:
        data_list.append(row)

with open(json_file,"w",encoding="utf-8") as f:
    json.dump(data_list,f,indent=4)