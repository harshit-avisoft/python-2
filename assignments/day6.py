# Bank Management System
class Bank:
    def __init__(self,account_number,account_holder_name,balance=0):
       self.account_number=account_number
       self.account_holder_name=account_holder_name
       self.balance=balance
    
    
    def deposit(self, amount) :
        if(amount>0):
            self.balance+=amount
        else:
            print("amount must be positive")
    def withdraw(self, amount):
        if(self.balance>=amount):
            self.balance-=amount
        else:
            print(f"your {amount} is greater than balance")

    def check_balance(self):
        print(self.balance)


acc1=Bank(100,"Harshit",95000)
acc2=Bank(101,"Ravi",54000)
acc3=Bank(102,"Raj",64000)
thisdict={
    acc1.account_number:acc1,
    acc2.account_number:acc2,
    acc3.account_number:acc3
}
temp="y"
while(temp=="y"):
 print("\n=====Menu=====")
 print("1: Deposit: ")
 print("2: Withdraw: ")
 print("3: Check balance: ")
 num=input("enter your choice(1/2/3) ")
 while num not in ("1","2","3"):
     print("Invalid Choice! please select from the menu")
     num=input("Enter valid choice(1/2/3) ")


 if num=="1":
    account_number=int(input("\nEnter your account number: "))
    if account_number in thisdict:
        amount=input("Enter amount to deposit: ")
        while not amount.isdigit():
              amount=input("Enter valid amount to deposit: ")
        amount=int(amount)
        thisdict[account_number].deposit(amount)
    else:
        print("invalid account number")
    temp = input("Do you want to continue? (y/N): ").strip().lower()


 if num=="2":
    account_number=int(input("\nEnter your account number: "))
    if account_number in thisdict:
        amount=input("Enter amount to withdraw: ")
        while not amount.isdigit():
              amount=input("Enter valid amount to withdraw: ")
        amount=int(amount)
        thisdict[account_number].withdraw(amount)
    else:
        print("invalid account number")
    temp = input("Do you want to continue? (y/N): ").strip().lower()


 if num=="3":
    account_number=int(input("\nEnter your account number: "))
    if account_number in thisdict:
       thisdict[account_number].check_balance()
    temp = input("Do you want to continue? (y/N): ").strip().lower()
