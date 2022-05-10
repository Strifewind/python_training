
#determine letter grade from given score
score = input("Enter Score: ")

try:
    score = float(score)
except:
    print("Score is outside nominal range")
if score >= 0.9:
    #some value
    print("A")
elif score >=0.8:
    #some value
    print("B")
elif score >=0.7:
    #some more value
    print("C")
elif score >=0.6:
    #even more value
    print("D")
else:
    #the student falied
    print("F")