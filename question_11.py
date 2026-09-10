students={
    "Aman": [85, 92, 78],
 "Riya": [95, 88, 91],
 "Karan": [72, 65, 80],
 "Simran": [45, 92, 88],
 "Raj": [90, 91, 95]
    
}
c=0
avg=0
high=0
for i in students.keys():
    for j in students[i]:
        if j<40:
            print(i, "Has failed.")
    average=sum(students[i])/3
    if(average>avg):
          
        avg=average
        high =i
    if average>=90 and i in  students[i]>=85:
        print(i," Has got scholarship.")
        c+=1
    elif average>=80:
        print(i, " Has got distinction.")
    elif average>=60:
        print(i," Pass")
    else:
        print("Needs improvement.")  

        

print("Total no.of students eligible for scholarship: ",c,"\n","Highest average marks: ",avg,"\n","Highest scorer is:",high)
