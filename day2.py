Name=["Harshit","Ravi","Raj","Rishav","Aman"]
Grades=["C","B","A","E","F"]
Valid_grades=["A","B","C","D","E","F"]


value="Y"

while(value=="Y"):
 print("\n\n\n")
 print("1. add a new student")
 print("2. update student's record")
 print("3. remove a student")
 print("Student Data Updation .....")
 print("\n")
 user_data=int(input("enter your choice : "))

 if user_data==1:
    name1=input("enter your name : ")
    # print("The valid grades are A B C D E F")
    grade1=input("enter your grade : ")
    print("\n")
    
    if grade1 in Valid_grades:
        Name.append(name1)
        Grades.append(grade1)
        print("updated data .... \n")
        for n, g in zip(Name, Grades):
         print(f"{n} : {g}")
        value=input("\n press N to exit and Y to continue...") 
    else:
         print("invalid grades not allowed")



 if user_data==2:
    name1=input("enter your name : ")
    # print("The valid grades are A B C D E F")
    grade1=input("enter your new grade : ")
    if name1 in Name and grade1 in Valid_grades:
        index=Name.index(name1)
        Grades[index]=grade1
        print("updated data .... \n")
        for n, g in zip(Name, Grades):
         print(f"{n} : {g}")
        value=input("\npress N to exit and  Y to continue...")    
    else:
        print("student doesn't exist or invalid grades")



 if user_data==3:
    name1=input("enter your name : ")
    if name1 in Name:
        index=Name.index(name1)
        Name.pop(index)
        Grades.pop(index)
        print("\n updated data .... \n")
        for n, g in zip(Name, Grades):
         print(f"{n} : {g}")
        value=input("\n press N to exit and  Y to continue...")
    else:
        print("student doesn't exist")
