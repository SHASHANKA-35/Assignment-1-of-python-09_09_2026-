marks=[78,45,91,33,67,49]
pas=0
fail=0
for i in marks:
    if(i>=40):
        print(i," Pass")
        pas+=1
    else:
        print(i," Fail")
        fail+=1
print("Required ratio= ",pas,":",fail)