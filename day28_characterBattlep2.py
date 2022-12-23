import time
import os
import random


def type1():
    char = input("1 What type is it?\n ")
    # print(names,"the",char)
    return char

def type2():
    char = input("2 What type is it?\n ")
    # print(names,"the",char)
    return char



def diceRoll(roll):
    
    guess=random.randint(1, roll)
    return guess


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

def charOneBattle():
    charOneScoreIn= diceRoll(6)
    return charOneScoreIn

def charTwoBattle():
    charTwoScoreIn= diceRoll(6)
    return charTwoScoreIn

def damage(outStrength1,outStrength2):
    a=outStrength1-outStrength2
    print("1 strength:",outStrength1)
    print("2 strength:",outStrength2)
    
    if a<0:
        a=(a*(-1))+1
        return a
    else:
        a=a+1
        return a



def charTwoBattle():

    charTwoScore=diceRoll(6)
    return charTwoScore

print("Character Batttle ")
time.sleep(1)
os.system("cls")
while True:
        
    names1 = input("1 Name your Legend's Name:")
    time.sleep(1)
    print()
    char1 = input("1 What type is it? ")
    outHealth1 = health()
    outStrength1= strength()
    time.sleep(1)
    os.system("cls")

    print()
    
    names2 = input("2 Name your Legend's Name:")
    char2 = input("2 What type is it? ")
    outHealth2 = health()
    outStrength2= strength()
    

    break
round=1
while outHealth1>=0 and outHealth2>=0:
    print("Round:",round)
    print(names1,"the",char1,"has a starting strength of",outStrength1,"and a Starting Health of:",outHealth1,"." )
    print()
    print(names2,"the",char2,"has a starting strength of",outStrength2,"and a Starting Health of:",outHealth2,"." )
    time.sleep(1.5)
    pause=input("")
    os.system("cls")
    
    charOneScore=charOneBattle()
    print(names1,"the",char1,"scored:" ,charOneScore,)
    
    
  
    
    charTwoScore=charTwoBattle()
    print(names2,"the",char2,"scored:" ,charTwoScore,)
    pause=input("")


    print("1 Health:",outHealth1)
    print("2 Health:",outHealth2)

    hit=damage(outStrength1,outStrength2)
    print(hit,"damage points are on the line")
    if charOneScore==charTwoScore:
        print("Tie, no winner, fight again")
        hit=0
    elif charOneScore>charTwoScore:
        print(names1,"the" ,char1,"wins the round by a score of",charOneScore,"to" ,charTwoScore,".")
        outHealth2=outHealth2-hit
        print(names2,"had their health reduced by",hit,"down to",outHealth2,".")

    elif charOneScore<charTwoScore:
        print(names2,"the" ,char2,"wins the round by a score of",charTwoScore,"to" ,charOneScore,".")
        outHealth1=outHealth1-hit
        print(names1,"had their health reduced by",hit,"down to",outHealth1,".")

    #hit=damage(outStrength1,outStrength2)
    if outHealth1<0:
        print(names2,"the",char2,"has killed" ,names1,"the",char1)
    elif outHealth2<0:
        print(names1,"the",char1,"has killed" ,names2,"the",char2)
    round+=1
    
    if outHealth1>=0 and outHealth2>=0:
        print("NEXT ROUND")  
    else:
        print("GAME OVER")
        


# print(outHealth)
# print(outStrength)
