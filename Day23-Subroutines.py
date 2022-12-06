def login():
    correctUser = "Cam"
    correctPass = "enter"

    while True:
        user = input("Enter your Username: ")

        passs = input("Enter your Password: ")
        if user != correctUser or passs != correctPass:
            print("Whoops I didn'trecognize that username or password.")
            print("Try Again")
            continue
        else:
            print("Welcome to Replit!")
            break


login()
# replit100DaysOfCode
