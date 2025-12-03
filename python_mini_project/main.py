import json
import os
from datetime import datetime, date

def load_inventory_data():
    if not os.path.exists("inventory_data.json"):
        return {}
    try:
        with open("inventory_data.json", "r") as file:
            raw_data = json.load(file)
        cleaned_data = {}
        for key, value in raw_data.items():
            try:
                cleaned_data[int(key)] = value
            except:
                return raw_data
        return cleaned_data
    except:
        print("Failed to load inventory file. Starting fresh.")
        return {}


def save_inventory_data(inventory):
    with open("inventory_data.json", "w") as file:
        json.dump(inventory, file, indent=4)

def log_transaction(entry_text):
    with open("transaction_log.txt", "a") as file:
        file.write(entry_text + "\n")

def create_backup(inventory):
    with open("backup_data.json", "w") as file:
        json.dump(inventory, file, indent=4)

def get_next_transaction_id():
    if not os.path.exists("transaction_id.txt"):
        with open("transaction_id.txt", "w") as file:
            file.write("1")
        return 1

    with open("transaction_id.txt", "r+") as file:
        data = file.read().strip()
        if data.isdigit():
            current_id = int(data)
        else:
            current_id = 1
        next_id = current_id + 1
        file.seek(0)
        file.write(str(next_id))
        file.truncate()
        return current_id



def log_transaction_dict(tx_type, product_id, qty_change, previous_quantity=None):
    tx_record = {
        "transaction_id": get_next_transaction_id(),
        "transaction_type": tx_type,
        "product_id": product_id,
        "quantity_changed": qty_change,
        "timestamp": datetime.now().strftime("%Y-%m-%d"),
        "previous_quantity": previous_quantity
    }
    with open("transaction_log.txt", "a") as file:
        file.write(json.dumps(tx_record) + "\n")


# Load inventory 
inventory = load_inventory_data()
transaction_history = []


# Validation Check
def validate_quantity_input(q):
    try:
        int(q)
        return True
    except:
        return False

def validate_price_input(p):
    try:
        float(p)
        return True
    except:
        return False

def validate_date_input(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except:
        return False

def validate_product_data(product):
    required_fields = [
        "product_name", "category", "current_quantity",
        "price_per_unit", "last_restock_date"
    ]

    for field in required_fields:
        if field not in product:
            print(f"Missing field: {field}")
            return False

    if not isinstance(product["product_name"], str) or not product["product_name"]:
        print("Invalid product name.")
        return False
    if not isinstance(product["category"], str) or not product["category"]:
        print("Invalid category name.")
        return False
    if not isinstance(product["current_quantity"], int) or product["current_quantity"] < 0:
        print("Quantity must be a non-negative integer.")
        return False
    if not isinstance(product["price_per_unit"], (int, float)) or product["price_per_unit"] <= 0:
        print("Price per unit must be a positive number.")
        return False
    if not validate_date_input(product["last_restock_date"]):
        print("Restock date format must be YYYY-MM-DD.")
        return False

    return True

#  Inventory Functions
def add_new_product():
    name = input("Product name: ").strip()
    while not name or name.isdigit():
        print("Product name can't be empty or only numbers.")
        name = input("Product name: ").strip()

    category = input("Category: ").strip()
    while not category or category.isdigit():
        print("Category can't be empty or only numbers.")
        category = input("Category: ").strip()

    qty_input = input("Initial quantity: ")
    while not validate_quantity_input(qty_input) or int(qty_input) <= 0:
        print("Enter a valid quantity (positive whole number).")
        qty_input = input("Initial quantity: ")

    price_input = input("Price per unit: ")
    while not validate_price_input(price_input) or float(price_input) <= 0:
        print("Enter a valid price (positive number).")
        price_input = input("Price per unit: ")

    qty = int(qty_input)
    price = float(price_input)

    if inventory.keys():
        new_product_id = max(inventory.keys()) + 1
    else:
        new_product_id = 1

    product = {
        "product_name": name,
        "category": category,
        "current_quantity": qty,
        "price_per_unit": price,
        "last_restock_date": str(date.today())
    }

    if not validate_product_data(product):
        return

    inventory[new_product_id] = product
    save_inventory_data(inventory)
    create_backup(inventory)
    log_transaction_dict("NEW_ITEM", new_product_id, qty, previous_quantity=0)
    print(f"Product added successfully with ID {new_product_id}.")


def update_product_quantity(product_id, change_amount):
    if product_id not in inventory:
        return "Invalid product ID."

    old_qty = inventory[product_id]["current_quantity"]
    new_qty = old_qty + change_amount
    if new_qty < 0:
        return "out of stock."
    inventory[product_id]["current_quantity"] = new_qty

    if change_amount > 0:
        inventory[product_id]["last_restock_date"] = str(date.today())

    save_inventory_data(inventory)
    if change_amount>0:
        tx_type="STOCK_ADD"
    else:
        tx_type="STOCK_REMOVE"

    log_transaction_dict(tx_type, product_id, change_amount, previous_quantity=old_qty)

    return f"Updated successfully. New quantity: {new_qty}"


def delete_product(product_id):
    if product_id not in inventory:
        return "Invalid product ID."

    product = inventory[product_id]
    print(f"\nProduct to delete: {product['product_name']} (ID: {product_id})")
    print(f"Category: {product['category']}, Quantity: {product['current_quantity']}, Price: {product['price_per_unit']}")

    confirm = input("Are you sure ? (yes/no): ").strip().lower()
    if confirm == "yes":
        del inventory[product_id]
        save_inventory_data(inventory)
        create_backup(inventory)
        log_transaction_dict("DELETE_ITEM", product_id, 0, previous_quantity=product["current_quantity"])
        return f"Product {product_id} deleted."
    else:
        return "Deletion cancelled."

def search_products(search_item):
    search_item = search_item.lower().strip()
    matches = []
    for pid, item in inventory.items():
        if search_item in item["product_name"].lower() or search_item in item["category"].lower():
            matches.append((pid, item))

    return matches

def display_inventory(category=None, ftype=None):
    if not inventory:
        print("Inventory is empty.")
        return
    header = (
        f"{'ID':<5}"
        f"{'Name':<20}"
        f"{'Category':<15}"
        f"{'Qty':<6}"
        f"{'Price':<10}"
        f"{'Restock':<12}"
    )
    print("\n----- Inventory -----")
    print(header)
    for pid, item in inventory.items():
        if ftype == "low_stock" and item["current_quantity"] >= 10:
            continue
        if ftype == "out_stock" and item["current_quantity"] > 0:
            continue
        if category and item["category"].lower() != category.lower():
            continue

        print(
            f"{pid:<5}"
            f"{item['product_name']:<20}"
            f"{item['category']:<15}"
            f"{item['current_quantity']:<6}"
            f"{item['price_per_unit']:<10.2f}"
            f"{item['last_restock_date']:<12}"
        )

def generate_inventory_report():
    total_items = len(inventory)
    total_value = 0
    low_stock = []
    out_of_stock = []
    category_totals = {}

    for pid, item in inventory.items():
        total_value += item["current_quantity"] * item["price_per_unit"]
        if item["current_quantity"] < 10:
            low_stock.append(pid)
        if item["current_quantity"] == 0:
            out_of_stock.append(pid)
        cat = item["category"]
        if cat in category_totals:
            category_totals[cat] += item["current_quantity"]
        else:
             category_totals[cat] = item["current_quantity"]

    if category_totals:
        most_stocked = max(category_totals, key=category_totals.get)
    else:
        most_stocked = "None"

    print("\n----- Inventory Summary -----")
    print("Total products:", total_items)
    print("Total inventory value:", total_value)
    print("Low stock items:", low_stock)
    print("Out of stock items:", out_of_stock)
    print("Category with highest total stock:", most_stocked)


def view_transaction_history():
    if not os.path.exists("transaction_log.txt"):
        print("No transaction history available.")
        return

    print("\n----- Transaction History -----")
    with open("transaction_log.txt", "r") as file:
        for line in file:
            try:
                his = json.loads(line.strip())
                print(
                    f"ID:{his['transaction_id']}  Type:{his['transaction_type']}  "
                    f"Prod:{his['product_id']}  Qty:{his['quantity_changed']}  "
                    f"Time:{his['timestamp']}  Prev:{his.get('previous_quantity')}"
                )
            except:
                print(line.strip())