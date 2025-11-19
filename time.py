duration=int(input("enter total seconds"))

min=(duration%3600)//60
hours=duration//3600
seconds=duration%60
print(f"{hours} hours {min} min {seconds} seconds")