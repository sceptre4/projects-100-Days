

year = int(input("What year is it?"))
secs = 60
min = 60
hour = 24
daySecs = (secs)*(min)*(hour)

regYearSecs = 365*(daySecs)
leapYearSecs = 366*(daySecs)


if year%4==0:
    if (year%100==0 and year%400!=0):
        print(str(year)+" isn't a Leap Year, so it has 365 days in it or",regYearSecs,"seconds. 100yes 400no")
    elif year%100==0 and year%400==0:
        print(str(year)+" is a Leap Year, so it has 366 days in it or",leapYearSecs,"seconds.")
    else:
        print(str(year)+" is a Leap Year, so it has 366 days in it or",leapYearSecs,"seconds by 4.")


else:
    print(str(year)+" isn't a Leap Year, so it has 365 days in it or",regYearSecs,"seconds. It isn't divisable by 4 evenly.")
