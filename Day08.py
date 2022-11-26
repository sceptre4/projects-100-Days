name = input("What's your name?")
name = name.title()
print(name)
age = input("And " + (name) + "," + " how old are you?")
while True:
    # how to do a while loop?
    if (age.isnumeric()) == True:
        break

    else:
        print("Using Numbers Please.")
        break

age = int(age)
if (age) <= 10:

    if age <= 4:
        print("", name, ",someone's writing this for you.")
    elif age <= 8:
        print("Dang", name, ",you're really smart to be typing at age", age, ".")
    else:
        print("Damm", name, "you're too young to be coding")
elif (age <= 25) and age >= 11:
    print("Darn", name, "at", age, "years old now is the time to be at school.")
elif (age <= 50):
    print("At the age of", age, "it's the time to be at work.")
job = input("Do you have a job?")
job = (job).title()
if job == "Yes" and age > 65:
    print("Well, you should be retired")
elif job == "No" and age < 50:
    print("Get a Job")
elif job == "No":
    print("Well, keep trying.")
else:
    Print("Well, do what pleases you.")
