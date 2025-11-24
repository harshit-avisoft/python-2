# text files
file=open("data.txt","r")

# r--read
# w==write(overwrite files)
# a--append
# r+--read + write

# read whole file
with open("data.txt","r") as f:
    content=f.read()
    print(content)

# read one line
with open("data.txt","r") as f:
    line=f.readline()
    print(line)

# read all lines
with open("data.txt","r") as f:
    lines=f.readlines()
    print(lines)

# write to a file
with open("data.txt","w") as f:
    f.write("hello world\n")

# append
with open("data.txt","a") as f:
    f.write("New line added\n")

# reading csv files
import csv
with open("data.csv",newline="") as f:
    content=csv.reader(f)
    for row in content:
        print(row)

# writing csv files
import csv
with open("students.csv","w",newline="") as f:
      content=csv.writer(f)
      content.writerow(["name","age"])
      content.writerow(["Harshit",20])
      content.writerow(["Ravi",22])

# read csv as dictionary
import csv
with open("data.txt","r",newline="") as f:
    content=csv.DictReader(f)
    for row in content:
        print(row["name",row["age"]])

# writing csv as dictionary
import csv
with open("marks.csv","w",newline="") as f:
    fieldnames=["name","math","science"]
    writer=csv.DictWriter(f,fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({"name":"Harshit","math":90,"science":85})



# reading json files
import json
with open("data.json","r") as f:
    data=json.load(f)

print(data)
print(data["name"])

# writing json file
import json

data={
    "name":"Harshit",
    "age":20,
    "city":"Delhi"
}

with open("data.json","w") as f:
    json.dump(data,f,indent=4)

# converting json string to python
import json
s='{"name":"Harshit","age":20}'
data=json.loads(s)

print(data)


# converting python object to json string

import json
obj={"a":1,"b":2}
json_string=json.dumps(obj)

print(json_string)
