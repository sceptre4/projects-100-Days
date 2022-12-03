
round = 1
player1Score = 0
player2Score = 0
winningScore=int(input("What number of wins, will win the game?"))
from getpass import getpass as input
print("The first player to",winningScore,"wins the game.")
while True:
    print("Select your move (R, P, or S)")
    input1 = input("Player 1 - Enter your choice, and hit the enter Key")
    input2 = input("Player 2 - Enter your choice, and hit the enter Key")

    if input1 == "R":
        if input2 == "R":
            print("Tie, Both players chose Rocks in Round ",round,".")
            round+=1
            continue
        elif input2 == "S":
            print ("Player 1 wins Round " ,round, ". Their Rock beat Scissors.")
            round+=1
            player1Score+=1
            if player1Score>=winningScore:
                print("*******Player 1 WINS the Tournament in round",round,"******* by a score of",player1Score,"to",player2Score)
                break
            else:
                print("The score is, Player1:",player1Score," to Player2:",player2Score,".")
                continue
        elif input2 == "P":
            print("Player 2 wins round",round,",their Paper beat Rocks.")
            round+=1
            player2Score+=1
            if player2Score>=winningScore:
                print("*******Player 2 WINS the Tournament in round",round,"******* by a score of",player1Score,"to",player2Score)
                break
            else:
                print("The score is: ",player1Score," : ",player2Score,".")
                continue
        else:
            print("Player 2 must enter a R or S or a P.")     
            continue

    elif input1 == "P":
        if input2 == "P":
            print("Tie, Both players chose Paper in Round ",round,".")
            round+=1
            continue
        elif input2 == "S":
            print("Player 2 wins round",round, "their Scisssors beats Paper.")
            round+=1
            player2Score+=1
            if player2Score>=winningScore:
                print("*******Player 2 WINS the Tournament in round",round,"******* by a score of",player1Score,"to",player2Score)
                break
            else:
                print("The score is: ",player1Score," : ",player2Score,".")
                continue

        elif input2 == "R":
            print("Player 1 wins, their Paper beats Rocks.")
            round+=1
            player1Score+=1
            if player1Score>=winningScore:
                print("*******Player 1 WINS the Tournament in round",round,"******* by a score of",player1Score,"to",player2Score)
                break
            else:
                print("The score is: ",player1Score," : ",player2Score,".")
                continue

        else:
            print("Try Again Player 2. You must enter a R or a S or P.")
            continue

    elif input1 == "S":
        if input2 == "S":
            print("Tie, Both players chose Scissors in Round ",round)
            round+=1
            continue
        elif input2 == "R":
            print("Player 2 wins round",round, "their Rocks beat Scissors.")
           
            player2Score+=1
            if player2Score>=winningScore:
                print("*******Player 2 WINS the Tournament in round",round,"******* by a score of",player1Score,"to",player2Score)
                round+=1
                break
            else:
                print("The score is: ",player1Score," : ",player2Score,".")
                round+=1
                continue

        elif input2 == "P":
            print("Player 1 wins round",round,"their Scissors beats Paper.")
            
            player1Score+=1
            if player1Score>=winningScore:
                print("*******Player 1 WINS the Tournament in round",round,"******* by a score of",player1Score,"to",player2Score)
                round+=1
            else:
                print("The score is: ",player1Score," : ",player2Score,".")
                round+=1
                continue
        else:
            print("invalid entry for input2")
    elif input1 != "R" or "S" or "P":
        print("Player 1 must enter a R or S or P")

    else:
        print("Try again, both players must enter a R or S or a P.")
