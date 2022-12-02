from getpass import getpass as input
round = 1
player1Score = 0
player2Score = 0
while True:
    print("It's Round ", round, ".")
    print("Select your move (R, P, or S)")
    input1 = input("Player 1 - Enter your choice, and hit the enter Key")
    input2 = input("Player 2 - Enter your choice, and hit the enter Key")

    if input1 == "R":
        if input2 == "R":
            print("Tie, Both players chose Rocks.")
        elif input2 == "S":
            print("Player 1 wins, their Rock beat Scisssors.")
        elif input2 == "P":
            print("Player 2 wins, their Paper beat Rocks.")
        else:
            print("Player 2 must enter a R or S or a P.")

    elif input1 == "P":
        if input2 == "P":
            print("Tie, Both player chose Paper.")
        elif input2 == "S":
            print("Player 2 wins, their Scisssors beats Paper.")
        elif input2 == "R":
            print("Player 1 wins, their Paper beats Rocks.")
        else:
            print("Player 2 must enter a R or a S or P.")

    elif input1 == "S":
        if input2 == "S":
            print("Tie, Both players choose Scissors")
        elif input2 == "R":
            print("S<R")
        elif input2 == "P":
            print("S>P")
        else:
            print("invalid entry for input2")
    elif input1 != "R" or "S" or "P":
        print("Player 1 must enter a R or S or P")

    else:
        print("Try again, both players must enter a R or S or a P.")
