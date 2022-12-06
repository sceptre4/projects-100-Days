'''
def whichCake(ingredient,base,coating):
  if ingredient=='chocolate':
    print("mmm, I love chocolate")
  elif ingredient=="brocalli":
    print("You What Mate?")
    
  else:
    print("yeah, that would be great too I suppose.")
  print("So you want a,",ingredient, "cake on a",base,"base with",coating, "on top")

whichCake("carrot","biscuit","icing")
'''
'''
def pizza_order(topping1, topping2):
  if topping1 == "pepperoni":
    print(topping1, "is a great choice")
  else:
    print(topping1, "is kinda lame on pizza")
  print(topping2, "sounds delicious, much better than", topping1)
'''
'''
topping1 =  input("Name a pizza topping. ")
topping2 = input("Name a second pizza topping. ")
'''
'''
pizza_order(
    "chicken", "topping2")
    #when I enter a parameter with subroutine it becomes a variable, unless entered as string.
'''
def dice(diceSides):
    import random
    
    while True:
        num=random.randint(1,diceSides)
        print("You rolled a",num)
        again=input("Roll Again?")
        if again=="No"or again=="no":
            exit()
        else:
            continue


    
diceSides=int(input("How Many Sided dice shall be rolled?")) 
dice(diceSides)

# replit100DaysOfCode 
'''
Solution:
import random
print("Infinity Dice 🎲")
  
sides = int(input("How many sides?: "))
playGame = "yes"
  
def rollDice(sides):
  print("You rolled ", random.randint(1,sides))
while playGame == "yes":
    rollDice(sides)
    playGame = input("Roll again?")
    '''