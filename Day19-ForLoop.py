
loan=1000
int=0
totalInterest=0
for i in range(10):
    int=(loan*.05)
    int=round(int,2)
    loan+=int
    totalInterest+=int
    
    
    print("Year",i+1,"is",loan)
print("You paid $",totalInterest," in interest!")

