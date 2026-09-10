transactions = {
 "Aman": [500, 1200, 300, 15000, 700],
 "Riya": [200, 300, 450, 600],
 "Karan": [10000, 50, 80, 12000],
 "Simran": [400, 500, 600, 700]
}
highest=0
high_person=""
suspicious=0
for i in transactions.keys():
    total=0
    sus=0

    for j in transactions[i]:
        total+=j
        if(j>10000):
            sus+=1
    if(sus>=2 or (sus==1 and total>=20000)):
        print(i," has done high risk transactions.")
    if(total>highest):
        highest=total
        high_person=i
    suspicious+=sus
    print(i," has spend total amount= ",total,"\n","For this person, total no.of suspicious transaction: ",sus)
print("The customer with the highest total spending is ",high_person,"\n"," He has spend total amount= ",highest)
print("Total number of suspicious transactions= ",suspicious)
