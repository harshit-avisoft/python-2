s1=int(input("enter first side of the triangle"))
s2=int(input("enter second side of the triangle"))
s3=int(input("enter third side of the triangle"))

if s1==s2==s3:
    print("equilateral triangle")
elif s1==s2 or s2==s3 or s1==s3:
    print("isosceles triangle")
else:
    print("scalene triangle") 
