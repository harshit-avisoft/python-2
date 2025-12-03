from main import (
    display_inventory,
    add_new_product, inventory,
    update_product_quantity, search_products,
    generate_inventory_report, create_backup,
    save_inventory_data, view_transaction_history, delete_product
)

# Menu Bar
def main_menu():
    while True:
        print("\n=== Inventory Management System ===")
        print("1. View Inventory")
        print("2. Add New Product")
        print("3. Update Stock")
        print("4. Search Products")
        print("5. Inventory Summary Report")
        print("6. View Transaction History")
        print("7. Delete Product")
        print("8. Save & Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            while True:
                print("\nSelect From Options:")
                print("1. Show all items")
                print("2. Low stock items (<10)")
                print("3. Out of stock items (=0)")
                print("4. Filter by specific category")

                choice = input("Choose anyone: ").strip()

                if choice == "1":
                    display_inventory()
                    break
                elif choice == "2":
                    display_inventory(ftype="low_stock")
                    break
                elif choice == "3":
                    display_inventory(ftype="out_stock")
                    break
                elif choice == "4":
                    category_name = input("Enter category name: ").strip()
                    if category_name:
                        display_inventory(category=category_name)  
                    else:
                        display_inventory()
                    break
                else:
                    print("Invalid choice. Try again.")

        elif choice == "2":
            add_new_product()

        elif choice == "3":
            while True:
                pid = input("Enter product ID: ").strip()
                if pid.isdigit() and int(pid) in inventory:
                    pid = int(pid)
                    break
                print("Invalid product ID. Try again.")

            while True:
                amount = input("Quantity change (+ / -): ").strip()
                try:
                    amount = int(amount)
                    break
                except ValueError:
                    print("Please enter a valid integer.")

            print(update_product_quantity(pid, amount))

        elif choice == "4":
            term = input("Search by name or category: ")
            results = search_products(term)

            if not results:
                print("No matching products found.")
            else:
                print(f"Found {len(results)} result(s):")
                for pid, item in results:
                    print(f"{pid}: {item['product_name']} ({item['category']}) | Qty: {item['current_quantity']} | Price: {item['price_per_unit']}")

        elif choice == "5":
            generate_inventory_report()

        elif choice == "6":
            view_transaction_history()

        elif choice == "7":
            while True:
                pid = input("Enter product ID to delete: ").strip()
                if pid.isdigit() and int(pid) in inventory:
                    pid = int(pid)
                    break
                print("Invalid product ID. Try again.")

            print(delete_product(pid))

        elif choice == "8":
            save_inventory_data(inventory)
            create_backup(inventory)
            print("Inventory saved. Backup created. Exiting program.")
            break

        else:
            print("Invalid option. Please select a valid number.")

main_menu()