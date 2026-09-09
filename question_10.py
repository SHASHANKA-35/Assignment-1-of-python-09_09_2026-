products={
    "laptop":{"price":50000,"stock":3},
    "phone":{"price":30000,"stock":5},
    "headphones":{"price":20000,"stock":0}
}
a=input("Enter the product name: ")
b=int(input("Enter the quantity of the product you want to purchase."))
if(a in products.keys()):
    if(b <=products[a]["stock"]):
        if(products[a]["price"]*b>50000):
            print("Congratulations, you have received 10 percent discount. You have to now pay only: ",0.9*products[a]['price']*b)
        else:
            print("You have to pay: ",products[a]["price"]*b)
    else:
        print("The quantity of the product you want is unavailable.")
else:
    print("The product is unavailable.")
