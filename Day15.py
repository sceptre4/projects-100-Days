'''animal=""
quit = ""
sound= ""


while quit!=("Yes"):
    animal=input("What animal do you want?")
    if animal=="Cow":
        print("A",animal,"goes Moo")
    elif animal=="Sheep":
        print("A",animal,"goes Bah")
    elif animal=="Horse":
        print("A",animal,"goes Neh")
    else:
         print("The",animal," goes Awooga")
    quit=input("Do you want to Quit?")
'''


exit = "no"


while exit == "no":
    animal_sound = input("What animal sound do you want to hear?")

    if animal_sound == "cow" or animal_sound == "Cow":
        print("🐮 Moo")
    elif animal_sound == "pig" or animal_sound == "Pig":
        print("🐷 Oink")
    elif animal_sound == "sheep" or animal_sound == "Sheep":
        print("🐑 Baaa")
    elif animal_sound == "duck" or animal_sound == "Duck":
        print("🦆 Quack")
    elif animal_sound == "dog" or animal_sound == "Dog":
        print("🐶 Woof")
    elif animal_sound == "cat" or animal_sound == "Cat":
        print("🐱 Meow")
    else:
        print("I don't know that animal sound. Try again.")

    exit = input("Do you want to exit?: ")
