import emoji
correct=0
table=int(input("What Multiplication table do you wantto use?"))

start=1
end=4
attempts=end-start



for i in range(start,end,1):
    print(i,"X",table,"= ?  ")
    answer=int(input("Your answer is:"))
    solution=i*table
    if answer==(solution):
        correct=correct+1
        print("correct")
    else:
        print("incorrect, the answer should have been",solution)
        
    
print("You got",correct,"correct out of",attempts)
if correct==attempts:
    print("you are awesome all correct")
    print("Wow! A perfect score! 🥳")
else:
    print("You missed",attempts-correct)
    
#replit100daysofcode