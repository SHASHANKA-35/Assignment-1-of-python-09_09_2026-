balance=float(input("Enter your account balance. "))
withdraw=float(input("Enter the amount you want to withdraw."))
if(withdraw<balance):
    print("Yes the withdraw is possible.\n","Remaining balance in your account is= ",balance-withdraw)
else:
    print("The amount of money you want to withdraw from your account is more than that present in it.")
