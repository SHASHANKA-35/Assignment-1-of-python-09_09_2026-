a=int(input("Enter a number:"))
if(a%2==0 and a>0):
    print("The number is even and positive.")
elif(a%2==0 and a<0):
    print("The number is even and negative.")
elif(a%2==0 and a==0):
    print("The number is even and zero.")
elif(a%2!=0 and a>0):
    print("The number is odd and positive.")
else:
    print("The number is odd and negative.")