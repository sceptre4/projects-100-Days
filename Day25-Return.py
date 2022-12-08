'''
def area_square(side1, side2):
  area = side1 * side2
  return area

area=area_square(4, 12)
print(area)
'''
import random
outcome=""
number=""


highSide=int(input("Pick how many sides"))
defaultName="Cam"
print("charactar stat generator")
name=input("Name your warrior: ")or defaultName

def firstDice():
    print("number sides = ",highSide)

   
    outcome=random.randint(1,highSide)
    
    
    print("The random dice roll, on a",highSide,"sided dice is",outcome,".")
    return outcome
choice=firstDice()
print("scope test",choice)
print("and the result from the outside is ",choice)

#6dice times 8dice




print("now comes the 2 dice part")
def health():
    h6=random.randint(1,6)
    print("6 sided dice is: ",h6)
    h8=random.randint(1,8)
    print("8 sided dice is: ",h8)
    health=h6*h8

    #print("the health score is:" ,health)
    return (health)

charhealth=health()

print("again the health score is: " ,charhealth)
#replit100DaysOfCode

'''
area = areaOfTriangle (5, 22)
print(area)
'''
