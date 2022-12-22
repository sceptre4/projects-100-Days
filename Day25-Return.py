'''
#subroutine has parameter called `number`
#`number` shows how many numbers we want the pin to have
def pinPicker(number):
    print(number)
    import random
    
    pin = "" 
    #this is the empty string
    for i in range(number):
         #for loop shows defined amount of random numbers
        pin += str(random.randint(0,9))
         #we want a string of random numbers between 0-9
        pin=int(pin)
    newpin=(pin)+1
    print(newpin)
    return newpin
    
pinPicker(4)
 #4 means we want 4 random numbers
'''

#subroutine has parameter called `number`
#`number` shows how many numbers we want the pin to have
def pinPicker(number):
  import random
  pin = "" #this is the empty string
  for i in range(number): #for loop shows defined amount of random numbers
    pin += str(random.randint(0,9)) #we want a string of random numbers between 0-9
    print(pin)
  return pin
    
pin=pinPicker(4) #4 means we want 4 random numbers
pin=int(pin)
print(pin+1)
