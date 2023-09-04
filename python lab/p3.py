s1=float(input("enter first side:"))
s2=float(input("enter second side:"))
s3=float(input("enter third side:"))
if s1<0 or s2<0 or s3<0:
   print("invalid output")
if (s1+s2>s3 or s2+s3>s1 or s3+s1>s2) and (s1>0 and s2>0 and s3>0):
    print("these sides form triangle")
   