#Author: Tyler R. Staut
#File Name: TylerStautLab19.py
#Date: 10/5/2015
#Description: Break and Continue Stuff

#-----STEP 1-----
print("Step 1:")
x = 1
while x <= 10:  #While it is less than 10
    if x > 4:
        break   #Breaks out of the loop, they cant keep him forever, "evil laugh"
    print(x, end=" ")
    x += 1
print("\n")
#----------------

#-----STEP 2-----
print("Step 2:")    
for x in range(1, 10):  #Prints a range of numbers
    if x == 5:
        continue    #Goes back to range
    print(x, end=' ')
print('\n')
#----------------

#-----STEP 3-----
print("Step 3:")
print("This step involves only a definition so you wont be able to see it in the console.")
def valid_number(age):      #Definition for age
    if (1 <= age <= 120):
        return True     #Returns True
    else:
        return False    #Returns False
#----------------

#-----STEP 4-----
print("Step 4:")

while True:     #Loop, does what it says.
    num_age = int(input("Age: "))       #Input the age
    if valid_number(num_age) == True:       #Check if age is True
        break       #Makes it go to the Thank You outside of loop
    if valid_number(num_age) == False:      #Check if age is False
        print("Invalid age, please enter another.")     #If false go through again
        continue    #Makes it go back to age input
print("Thank You!") 
#----------------
        
    