'''
def pinpicker(number):
    import random
    pin=""
    for i in range(number):
        pin=pin+str(random.randint(0,9))
    return pin

myPin=pinpicker(9)
print(myPin)
'''
import random
outcome=""
highSide=int(input("Pick how many sides"))

def firstDice(number):
    print("number sides =",highSide)

   

    
    
    print("The random dice roll, on a",highSide,"sided dice is",outcome,".")
outcome=random.randint(1,highSide)
firstDice(outcome)