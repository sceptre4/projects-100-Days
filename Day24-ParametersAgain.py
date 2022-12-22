'''
def dice1(sidesd1):
    import random
    roll1=random.randint(1,sidesd1)
    return roll1

sidesd1=int(input("Enter sides of dice"))
roll1=dice1(sidesd1)
print(roll1)
'''
def dice2and3():
        import random
        
        d2=random.randint(1,6)
        
        d3=random.randint(1,8)
        health=d2*d3
                
        print()
            
        print("the health score is",health)
            
        print("1 to Go Again")
        print("2 to Quit")
        again=input("1 or 2: ")
        again=int(again)
        while again==1:
            print ("Let's try again")
            dice2and3()
            if again==2:
                print("Ok,Quit")
                break
            else:
                break
         
health=dice2and3()
print("outside")

