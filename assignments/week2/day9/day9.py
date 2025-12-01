import re

# 1
def word_presence_checker():
    sentence = input("Enter a sentence: ")
    word = input("Enter a word to search for: ")
    if sentence == "" or word == "":
        print("Invalid input")
    else:
        pattern = rf"\b{word}\b"
        match = re.search(pattern, sentence)
        if match:
            print(f"Yes, the word '{word}' exists in the sentence.")
        else:
            print(f"The word '{word}' does not exist in the sentence.")

# 2
def number_extraction():
    sentence = input("Enter a sentence: ")
    integers = re.findall(r"\b\d+\b", sentence)
    integers = list(map(int, integers))
    print("Extracted integers:", integers)

# 3
def extract_patterns():
    sentence = input("Enter a sentence: ")
    pattern1 = r"Order ID\s*:\s*([A-Za-z]+-\d+)"
    pattern2 = r"warehouse\s*(\d+)"
    warehouses = re.findall(pattern2, sentence)
    orders = re.findall(pattern1, sentence)
    print("Order IDs:", orders)
    print("Warehouses:", warehouses)

# 4
def clean_up():
    sentence = input("Enter a sentence: ")
    sentence = re.sub(r'\W', " ", sentence)
    sentence = re.sub(r'\s+', " ", sentence)
    print("Cleaned sentence:", sentence)

# 5
def email_validation():
    email = input("Please enter a valid email: ")
    pattern = r'^[\w][\w\W]*@[\w\W]*[\.]+[\w\W]*'
    match = re.search(pattern, email)

    if match:
        print("Your email is valid.")
    else:
        print("Invalid email entered.")


def menu():
  while True:
    print("\n----- MENU -----")
    print("1. Word Checker")
    print("2. Extract Number")
    print("3. Extract Patterns")
    print("4. Clean Up ")
    print("5. Validate email")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        word_presence_checker()
    elif choice == "2":
        number_extraction()
    elif choice == "3":
        extract_patterns()
    elif choice == "4":
        clean_up()
    elif choice == "5":
        email_validation()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 6.")

# Run the menu
menu()
