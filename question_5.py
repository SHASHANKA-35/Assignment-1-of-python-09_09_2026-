a=int(input("Enter the no.of units consumed."))
bill=0
if(a<=100):
    bill=a*2
elif(a<=200):
    bill=100*2+(a-100)*3
else:
    bill=100*2+100*3+(a-200)*5
print("Total bill amount= ",bill)