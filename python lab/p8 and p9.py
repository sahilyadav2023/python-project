bs=int(input("enter basic salary"))
hra=0.2*bs
ta=0.05*bs
da=0.1*bs
gs=bs+hra+ta+da
print(gs)
# question 9
if gs<300000:
  print("income tax is",0*gs)
if gs>=300000 and gs<1000000:
   print("income tax is",0.1*gs)
if gs>=1000000 and gs<2500000:
   print("income tax is",0.2*gs)
if gs>=2500000:
   print("income tax is",0.3*gs)
   