
count = 1

while True:
    print("Never going to ______ you up.")
    answer = input("What's the missing word?")
    print(answer)
    if answer == "give":
        print("Well done, it only took you ", count, " attempt(s).")
        break
    else:
        print("Nope, try again.")
        count += 1


'''   



Never going to ______ you up.
let
Nope, try again.

Never going to ______ you up.
give

Well done! It only took you 3 attempts.
'''
