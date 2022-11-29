myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tipAmount = float(input("What % tip should they get?"))

tipAmount = tipAmount/100
myBill = myBill*(1+tipAmount)
answer = myBill / numberOfPeople
answer = round(answer, 2)
print("You each owe $"+str(answer)+".")
