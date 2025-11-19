Name=["Harshit","Ravi","Raj","Rishav","Aman"]
Grades=["C","B","A","E","F"]
Valid_grades=["A","B","C","D","E","F"]


user_data=0

while(user_data!=4):
 print("\n\n\n")
 print("1. add a new student")
 print("2. update student's record")
 print("3. remove a student")
 print("4. if you want to exit press ")
 user_data=int(input("enter your choice : "))

 if user_data==1:
    name1=input("enter your name : ")
    print("The valid grades are A B C D E F")
    grade1=input("enter your grade : ")
    print("\n")
    
    if grade1 in Valid_grades:
        Name.append(name1)
        Grades.append(grade1)
        for n, g in zip(Name, Grades):
         print(f"{n} : {g}")
    else:
         print("invalid grades not allowed")



 if user_data==2:
    name1=input("enter your name : ")
    print("The valid grades are A B C D E F")
    grade1=input("enter your new grade : ")
    if name1 in Name and grade1 in Valid_grades:
        index=Name.index(name1)
        Grades[index]=grade1
        print(Name)
        print(Grades)
    else:
        print("student doesn't exist or invalid grades")



 if user_data==3:
    name1=input("enter your name : ")
    if name1 in Name:
        index=Name.index(name1)
        Name.pop(index)
        Grades.pop(index)
        print(Name)
        print(Grades)
    else:
        print("student doesn't exist")
