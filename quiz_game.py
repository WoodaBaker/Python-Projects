print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play!")
score = 0

answer_1 = input("What does CPU stand for? ")
if answer_1.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer_2 = input("What does GPU stand for? ")
if answer_2.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer_3 = input("What does RAM stand for? ")
if answer_3.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/3) * 100) + "%.")
