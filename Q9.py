bs=int(input("Enter basic salary: "))
HRA=0.2*bs
TA=0.5*bs
DA=0.1*bs
GS=bs+HRA+TA+DA
print("The gross salary is ",GS)
if GS<300000:
    print("The income tax",GS)
if GS>300000 and GS<1000000:
    print("The income tax is",0.1*GS)
if GS>1000000 and GS<2500000:
    print("The income tax is",0.2*GS)
if GS>2500000:
    print("The income tax is",0.3*GS)
