

year = int(input("What year is it?"))
secs = 60
min = 60
hour = 24
daysecs = (secs)*(min)*(hour)

regyearsecs = 365*(daysecs)
leapyearsecs = 366*(daysecs)


leapyear = ""


if year % 400 == 0 and year % 100 == 0 and year % 4 == 0:
    print("There are", leapyearssecs, "seconds in this leap year.400")
elif year % 4 == 0:
    print("There are", leapyearssecs, "seconds in this leap year.4")
elif year % 4 == 0:
        print("Yes, it's 400 100 and 4")
else:
        print("no, divisable by 100 and 400, but not 4")
elif year % 4 == 0:
        print("Yes, its leap")

"""
