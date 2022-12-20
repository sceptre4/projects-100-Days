import time
import os

print("Character Builder")


def names():

    names = input("Name your Legend's First Name:")
    return names


def type():
    char = input("What type is it? ")
    # print(names,"the",char)
    return char

    # char()

def diceRoll(roll):
    import random
    random.randint(1,roll )
    return roll

def health():
    
    d6 = diceRoll(6)
    d12 = diceRoll(12)
    health = (((d6*d12)/2)+10)
    return health


def strength():
    
    d6 = diceRoll(6)
    d12 = diceRoll(12)
    strength = (((d6*d12)/2)+12)
    return strength


while True:
    namesOut = names()
    charTypeout = type()
    print(namesOut, "the", charTypeout)
    outStrength = strength()
    print("Strength is", outStrength)
    print()
    outHealth = health()
    print("Health is", outHealth)

    again = input("Y to create another character ")
    if again == "Y":
        continue
    else:
        # print("test")
        break

# print(outHealth)
# print(outStrength)
