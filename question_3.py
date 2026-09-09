a=int(input("Enter the marks"))
if(a<0 or a>100):
    print("Invalid marks")
elif(a>90):
    print("A")
elif(a>80):
    print('B')
elif(a>75):
    print('C')
else:
    print("Fail")