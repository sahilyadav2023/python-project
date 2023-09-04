s1=int(input("Enter the side1: "))
s2=int(input("Enter the side2: "))
s3=int(input("Enter the side3: "))
if s1<0 or s2<0 or s3<0:
    print("Enter a valid side")
if (s1+s2>s3 or s1+s3>s2 or s2+s3>s1) and (s1>0 or s2>0 or s3>0):
    print("All three sides form triangle ")
else:
    print("Not a triangle")