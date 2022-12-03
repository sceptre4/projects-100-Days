# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)
# generate some integers
for _ in range(1):
    randNumber = randint(1, 1000000)
    # print(randNum)
attempt = 0
print(randNumber)

guess = int(input("Between 1 and a Million"))
print(guess)

while True:
    guess = int(input("Between 1 and a Million"))
    print(guess)

    if guess < 0:
        quit()
    elif guess == randNumber:
        print("Winner")
        attempt += 1
        break
    elif guess < randNumber:
        print("YOur guess is Too Small")
        attempt += 1
        continue
    elif guess > randNumber:
        print("Your guess is Too Big")
        attempt += 1
        continue
    else:
        print("why")
        break
print("the number was guessed in", attempt, "tries.")
