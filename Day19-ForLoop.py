
loan=1000
interest=0
apr=0.05
totalInterest=0
for i in range(10):
    loan+=(loan*apr)
    interest+=loan*apr
    totalInterest+=interest
    

    
    
    
    print("Year",i+1,"is",loan)
print()    
print("You paid $",totalInterest," in interest!")

