#Name: Matthew Newton Bowen
#File Name: MatthewBowenLab17
#Date: 30 September 2015
#Description: Converting loops

#-----Step 1-----
print("Step 1:\n")
x = 20
while x > 0: #Loop from x = 20 to 0
    print(x)
    x-=2
print(" ")

#-----Step 2-----
print("Step 2:\n")
for a in range(0,101,10): #Loop will print each multiple of 10 from 0 to 100
    print(a, end = " ")
print(" \n")

#-----Step 3-----
print("Step 3:\n")
print("The answer to step 3 is no; it can not be done.\n")

#-----Step 4-----
x=0
print("Step 4:\n") #These loops print a certain amount of stars
for x in range(0,11):
    print("*", end=" ")
print(" ")
for x in range(0,6):
    print("*", end=" ")
print(" ")
for x in range(0,21):
    print("*", end=" ")
print("\n")

#-----Step 5-----
print("Step 5:\n") #This will print a 10 x 10 grid of stars
for x in range(1,11):
    for y in range(1,11):
        print("*", end=" ")
    print(" ")
print("\n")

#-----Step 6-----
print("Step 6:\n") #This will print the numbers from 0 to 9 on each line, starting at 0 and increasing by 1
for x in range(11):
    for y in range(x):
        print(y, end=" ")
    print(" ")
