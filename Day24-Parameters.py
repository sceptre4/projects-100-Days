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


    '''
    This subroutine creates a random pin number for us. This subroutine (called `pinPicker`) has the parameter called `number` (how many numbers I want to have in this pin). Then, there is a string (called `pin`) that is empty and a `for` loop that is used to create a defined amount of random numbers. The variable `number` controls how many times the loop will add the new number to the pin. This is done through `+=` and concatenating new values. We will cast the random number as a string so it can be concatenated together. 

Then...the magic...we `return` the pin.

👉 Let's see what happens:

```python
#subroutine has parameter called `number`
#`number` shows how many numbers we want the pin to have
def pinPicker(number):
  import random
  pin = "" #this is the empty string
  for i in range(number): #for loop shows defined amount of random numbers
    pin += str(random.randint(0,9)) #we want a string of random numbers between 0-9
  return pin
    
pinPicker(4) #4 means we want 4 random numbers
```

## Nothing happens? Why?

The line `pinPicker(4)` that calls for a 4 digit pin is being replaced by a 4 digit pin. (That's great, but I don't see that happening...)

We are not telling the computer to do anything with the string that was created. How do we make the string appear?

With `print` of course!

👉 Let's assign a variable to `pinPicker`:

```python
myPin = pinPicker(4)
'''