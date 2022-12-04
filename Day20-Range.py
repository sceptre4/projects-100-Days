#Thirteen times table
#for i in range(1,13,1):
 #   print(i,"times 13=",i*13)



start=input("Give Starting Number: ")
start=int(start)
print()
end=input("Give Ending Number: ")
end=int(end)
print()
inc=input("Give Increment: ") 
inc=int(inc)
print()
print("Start at",start,". ""End at",end,"." "Increment at",inc,".")
print()
for i in range(start,end+1,inc):
    print(i)
#replit100daysofcode