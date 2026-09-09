print("Enter the length of the 3 sides of a triangle.")
a=int(input( ))
b=int(input())
c=int(input())
if((a+b)>c and b+c>a and c+a>b):
    if(a==b==c):
        print("It is an equilateral triangle.")
    elif(a==b or b==c or c==a):
        print("It is an isoscele triangle.")
    else:
        print("It is a scalene triangle.")
else:
    print("It is not a valid triangle.")