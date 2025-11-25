# Bank Management System
class Bank:
    def __init__(self,account_number,account_holder_name,balance=0):
       self.account_number=account_number
       self.account_holder_name=account_holder_name
       self.balance=balance
    
    
    def deposit(self, amount) :
        self.balance+=amount
   
    def withdraw(self, amount):
        self.balance-=amount

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
print("Enter 1 deposit: ")
print("Enter 2 to withdraw: ")
print("Enter 3 to check balance: ")
num=int(input("enter your choice: "))

if num==1:
    account_number=int(input("\nEnter your account number: "))
    if account_number in thisdict:
        amount=int(input("Enter amount to deposit: "))
        thisdict[account_number].deposit(amount)
    else:
        print("invalid account number")

if num==2:
    account_number=int(input("\nEnter your account number: "))
    if account_number in thisdict:
        amount=int(input("Enter amount to deposit: "))
        thisdict[account_number].withdraw(amount)
    else:
        print("invalid account number")

if num==3:
    account_number=int(input("\nEnter your account number: "))
    if account_number in thisdict:
       thisdict[account_number].check_balance()