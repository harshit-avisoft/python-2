contacts = {
  "Harshit" : {
    "phone" : "961",
    "email" : 2004,
    "city" : "patna"
  },
  "Ravi" : {
    "phone" : "962",
    "email" : 2007,
    "city" : "jammu"
  },
  "Aman" : {
    "phone" : "963",
    "email" : 2011,
    "city" : "delhi"
  },
  "Rishav" : {
    "phone" : "964",
    "email" : 2006,
    "city" : "mumbai"
  },
  "Raj" : {
    "phone" : "965",
    "email" : 2000,
    "city" : "kashmir"
  }
}


value="Y"

while value=="Y":
    print("\n\n")
    print("------Contact record updation dashboard------")
    # print("\n")
    print("1. To Display All Contacts")
    print("2. search by contact name")
    print("3. search by city")
    print("4. add a new contact")
    print("5. update an existing contact")
    print("6. delete a contact ")
    print("\n")
    user_data=int(input("enter your choice [1-7] : "))

    if user_data==1:
       
        print("------------------------")

        for Name , details in contacts.items():
            print(f"Name: {Name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"city: {details['city']}")
            print("------------------------")

    if user_data==2:
        search = input("Enter  name: ").lower()
        temp=False
        for name, details in contacts.items():
            if search in name.lower():
                print("Name:", name)
                print("Phone:", details["phone"])
                print("Email:", details["email"])
                print("City:", details["city"])
                print("---------------------")
                temp=True
        
        if temp==False:
                print(" name not found ")

    if user_data==3:
        city1=input("enter city to search for : ").lower()
        temp=False
        for name , details in contacts.items():
            if city1 in details["city"].lower():
                print("Name:", name)
                print("Phone:", details["phone"])
                print("Email:", details["email"])
                print("city:", details["city"])
                print("---------------------")
                temp=True
        
        if temp==False:
                print("city not found")

    

    if user_data==4:
        name=input("Enter new name: ")
        if name in contacts:
            print("Name already exists")
        else:
            phone = input("Enter phone number: ")

            while not phone.isdigit() :
                 print("Please enter digits only!")
                 phone = input("Enter phone number: ")

            email = input("Enter email: ")
            while "@" not in email:
                print("enter valid email ")
                email = input("Enter email: ")
            city = input("Enter city: ")

            contacts[name] = {
                "phone": phone,
                "email": email,
                "city": city
            }
            print("Name added successfully")

    if user_data==5:
        name=input("Enter name whose details need to be updated: ")
        if name in contacts:
            phone = input("Enter phone number: ")

            while not phone.isdigit() :
                 print("\nPlease enter digits only!")
                 phone = input("Enter phone number: ")
                 
            email = input("Enter email: ")
            while "@" not in email:
                print("\nenter valid email ")
                email = input("Enter email: ")
            city = input("Enter city: ")

            contacts[name] = {
                "phone": phone,
                "email": email,
                "city": city
            }
            print("details updated successfully")
        else:
            print("Name not found")

    if user_data==6:
        name=input("Enter name to delete: ")
        if name not in contacts:
            print(f"{name} doesn't exist in database")
        else:
            del contacts[name]
            print("Contact deleted successfully")

    value=input("\npress N to exit and Y to continue...").upper()
    print("exited succesfully")
