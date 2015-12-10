from random import *

num_1 = randint(0, 10)

num_2 = randint(0, 10)

print("What is the total of ", num_1, " + ", num_2, "?")


total = num_1 + num_2

while True:
    if total == (int(input("Answer: "))):
        print("Congrats you have done it!")
        break
    else:
        print("Answer was wrong, try again.")
    

