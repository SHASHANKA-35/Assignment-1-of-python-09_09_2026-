stock={"laptop":5,
       "mouse":0,
       "keyboard":3,
       "monitor":0
}
prod=input("Enter product name: ")
if prod in stock.keys():
    if(stock[prod]!=0):
        print("Your product is present as well as available.")
    else:
        print("Your product is present but not available at the present.")
else:
    print("Your product is not present.")