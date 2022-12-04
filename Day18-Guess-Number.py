


attempt = 0
print(randNumber)




while True:
    guess = int(input("Between 1 and a Million  "))
    print(guess)
    print()
    if guess < 0:
        print("you're done")
        quit()
    elif guess == randNumber:
        print("Winner")
        attempt += 1
        print()
        break
    elif guess < randNumber:
        print("YOur guess is Too Small")
        attempt += 1
        print()
        continue
    elif guess > randNumber:
        print("Your guess is Too Big")
        attempt += 1
        print()
        continue
    else:
        print("why")
        print()
        break
print("the number was guessed in", attempt, "tries.")
randNumber=""