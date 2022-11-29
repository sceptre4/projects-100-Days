'''
Name of Exam
Max possible score
score recievd
convert to a %, to 2 decimal places, You got 79.00% which is a B

90% and above is an A+
80% is an A
70% is a B
60% is a C
50% is a D
40 is a U'''

exam = input("What was the name of the Exam?")
rawScore = int(input("What was your mark?"))
maxScore = int(input("Out of what?"))
scorePercent = ((rawScore/maxScore)*100)
scorePercent = round(scorePercent, 2)

if scorePercent >= 90:
    print(str(scorePercent)+"% is an A+.")
elif scorePercent >= 80:
    print(str(scorePercent)+"% is a A.")
elif scorePercent >= 70:
    print(str(scorePercent)+"% is a B.")
elif scorePercent >= 60:
    print(str(scorePercent)+"% is a C.")
elif scorePercent >= 50:
    print(str(scorePercent)+"% is a D.")
elif scorePercent >= 40:
    print(str(scorePercent)+"% is a U.")
else:
    print(str(scorePercent)+"% is a Failing Grade.")
