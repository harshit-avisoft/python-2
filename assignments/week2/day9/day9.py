import re

def word_presence_checker():
# 1
 sentence=input("Enter a sentence: ")
 word=input("Enter a word to search for: ")
 pattern=rf"\b{word}\b"
 match=re.search(pattern,sentence)
 if match:
    print(f"Yes the word {word} exists in the sentence: ")
 else:
    print(f"The word {word} not exists in the sentence: ")


def number_extraction():
# 2
 sentence=input("Enter a sentence: ")
 integers=re.findall(r"[\b][\d+][\b]",sentence)
 for integer in integers:
    print(integer)



def extract_patterns():
# 3
 sentence=input("Enter a sentence: ")
 pattern1=r"Order ID\s*:\s*([\w]+-(\d+))"
 pattern2=r"warehouse\s*(\d+)"
 warehouses=re.findall(pattern2,sentence)
 orders=re.findall(pattern1,sentence)
 for order in orders:
    print(order[0])

 for warehouse in warehouses:
    print(warehouse)


def clean_up():
# 4
 sentence=input("Enter a sentence: ")
 sentence=re.sub(r'\W'," ",sentence)
 sentence=re.sub(r'\s+'," ",sentence)
 print(sentence)



def email_validation():
# 5
 email=input("Please enter valid email: ")
 pattern=r'^[\w][\w\W]*@[\w\W]*[\.]+[\w\W]*'
 match=re.search(pattern,email)

 if match:
    print("Your email is valid: ")
 else:
    print("Invalid email entered: ")
 print("hi")