#Shauna Miletty
#P4HW1
#04/25/2025
#inputing scores using loops


"""
ask user to enter how many grades they would like to enter
program will collect all scores intetered
program will drop lowest score then modify the list
program will average the modified list
then display the results 
"""





score_num = int(input("How many scores do you need to enter? "))
print()

#empty list
scores = []

for num in range(1, score_num + 1):
    #collect scores
    score = float(input("Enter score #" + str(num)+ ":"))
    #evaluate entry
    while score < 0 or score > 100:
        print("INVALID SCORE ENTERED!!!")
        print("Score should be between 0 and 100")
        score = float(input("Enter score #" + str(num) +" again: "))

    scores.append(score)
    print()
                            
#find lowest score
if len(scores) > 1:
    lowest = min(scores)
    scores_modified = scores
else:
    lowest = scores[0]
#drop lowest score
    scores_modified.remove(lowest)

#calculate average
if len(scores_modified) > 0:
    avg = sum(scores_modified)/ len(scores_modified )

#determine letter grade for average
    if avg >= 90:
        grade = "A"

    elif avg >= 80:
        grade = "B"

    elif avg >= 70:
        grade =  "C"

    elif avg >= 60:
        grade = "D"

    else:
        grade = "F"

#display results

print("-----------------Results----------------------")
print(f"{'Lowest Score:':20} {lowest}")
print(f"{'Modified List:':20} {scores_modified}")
print(f"{'Scores Average:':20} {avg:.2f}")
print(f"{'Grade:':20} {grade}")
print("-----------------------------------------------")
