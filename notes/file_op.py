# opening a file
file=open("data.txt","r")
file.close()

# reading entire file
with open("data.txt","r") as f:
    content=f.read()
    print(content)

# read line by line
with open("data.txt","r") as f:
    content1=f.readline()
    content2=f.readline()
    print(content1 , content2)

with open("data.txt","r") as f:
    for line in f:
        print(line.strip())

# return list of lines
with open("data.txt","r") as f:
    lines=f.readlines()
    print(lines)

# writing to files -- overwrites
with open("data.txt","w") as f:
    f.write("Hello World\n")
    f.write("New line here\n")

# append
with open("data.txt","a") as f:
    f.write("This line is added at the end\n")
