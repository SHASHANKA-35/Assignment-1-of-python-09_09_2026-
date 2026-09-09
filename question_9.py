a=float(input("Enter the total shopping amount."))
print("Original amount:",a)
disc=0
if(a<1000):
    disc=0
elif(a<=4999):
    disc=0.1
elif(a<=9999):
    disc=0.2
else:
    disc=0.3
disc=disc*a
print("Discount amount= ",disc)
print("Final amount to be paid= ",a-disc)