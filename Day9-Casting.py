myScore = float(input("Your Score: "))
if myScore > 2000:
    print("winner!")
else:
    print("TRy again")

    # what generation are you from?
born = int(input("When were you born?"))
if born >= 1925 and born < 1947:
    if born == 1940:
        print("born in 1940")
    elif born >= 1941:
        print("born between 1941 and 1946")
    elif born >= 1925 and born <= 1939:
        print("born 1925 to 1939")
    else:
        print("born between 25 and 40 sometime")
elif born >= 1947 and born < 1965:
    print("You belong to the Baby Boomers")
else:
    print("whenever")
