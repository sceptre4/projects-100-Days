tvShow = input("what your favourite tv show? ")
if tvShow == "peppa pig":
    print("Ugh, why?")
    faveCharacter = input("Who is your favourite character?")
    if faveCharacter == "daddy pig":
        print("Right Answer")
    elif faveCharacter == "Daddy Pig":
        print("Correct, Capitialized")
    else:
        print("Nah, Daddy Pig's the greatest")
elif tvShow == "paw patrol":
    print("Sad Times")
else:
    print("Yeah, that's cool")
