import random
import json
from datetime import date
# Inventory Management System

product_dictionary={
    1:{
        "product_name":"Wire",
        "category":"Electronics",
        "current_quantity":0,
        "price_per_unit":10,
        "last_restock_date":"2025-12-01"
    },
    2:{
        "product_name":"Books",
        "category":"Stationary",
        "current_quantity":40,
        "price_per_unit":25,
        "last_restock_date":"2025-11-30"
    }
}

transaction_list=[]

def add_new_product():
    new_product=input("Enter name of the product: ")
    id=random.randint(1, 1000000)
    category=input("Enter the category: ")
    quantity=input("Enter the quantity: ")
    price=int(input("Enter the price of the product: "))
    last_restock_date=date.today()
    product_dictionary[id]={
        "product_name":new_product,
        "category":category,
        "current_quantity":quantity,
        "price_per_unit":price,
        "last_restock_date":last_restock_date
    }
    return id

def update_product_quantity1(product_id,change_amount):
    
    if change_amount>0:
        product_dictionary[product_id]["last_restock_date"]=date.today()
    product_dictionary[product_id]["current_quantity"]+=change_amount
    return f"success"

def update_product_quantity2():
    id=int(input("Enter product id of the user to be updated: "))
    change_amount=int(input("Enter amount to be added or removed: "))
    update_product_quantity1(id,change_amount)

def search_by_product_name(product_name):
    for key in product_dictionary.keys():
        if product_dictionary[key]["product_name"]==product_name:
            print(product_dictionary[key]["category"])
            print(product_dictionary[key]["current_quantity"])
            print(product_dictionary[key]["price_per_unit"])
            print(product_dictionary[key]["last_restock_date"])

def search_by_category(product_category):
    for key in product_dictionary.keys():
        if product_dictionary[key]["category"]==product_category:
            print(product_dictionary[key]["category"])
            print(product_dictionary[key]["current_quantity"])
            print(product_dictionary[key]["price_per_unit"])
            print(product_dictionary[key]["last_restock_date"])

def search_products():
    print("1. Enter product name")
    print("2. Enter categories: ")
    choice=int(input("Enter your choice: "))
    if choice==1:
        product_name=input("Enter product name: ")
        search_by_product_name(product_name)
    if choice==2:
        category=input("Enter the category: ")
        search_by_category(category)

# search_products()

def generate_inventory_report():
    print(len(product_dictionary),"is the total number of products: ")
    value=0
    temp1=0
    temp2=0
    low_stock_items=[]
    out_of_stock_items=[]
    most_stocked_category=[{}]
    for x, obj in product_dictionary.items():
        print(x)
        pass
        for y in obj:
        # print(y + ':', obj[y])
         if y=="current_quantity":
            temp1=obj[y]
            if obj[y]<10:
                low_stock_items.append(y)
            if obj[y]==0:
                out_of_stock_items.append(y)
         if y=="price_per_unit":
            temp2=obj[y]
            value+=temp1*temp2
    print(f"Total inventory value is {value}")
    print(f"Low stock items {low_stock_items}")
    print(f"out of stock items {out_of_stock_items}")




def display_inventory():
    print(json.dumps(product_dictionary, indent=4))


# error handling
def validate_product_data(product_data):
    pass

def validate_quantity_input(quantity):
    if type(quantity)!=int and quantity<=0:
        return False
    return True

def validate_price_input(price_str):
    if type(price_str)!=float:
        return False
    return True

def validate_date_Input(date_str):
    pass