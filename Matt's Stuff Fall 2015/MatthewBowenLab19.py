#Name: Matthew Newton Bowen
#File Name: MatthewBowenLab19
#Date: 05 October 2015
#Description: Break/Continue

#-----Step 1-----
print("Step 1:\n")
x = 1              
while x <= 10:       #Prints numbers from 1 to 4 
    if x == 5:
        break
    print(x)
    x+=1
print(" ")

#-----Step 2-----
print("Step 2:\n")
for x in range(1,10): #Prints numbers from 1 to 9, without 5
    if x == 5:
        continue
    print(x)
    x += 1
print(" ")

#-----Step 3-----
print("Step 3:\n")
def valid_number(age): #Defines this function
    if 1 <= age <= 120:
        return True
    else:
        return False
print(" ")
#-----Step 4-----
print("Step 4: ") #Takes age, if invalid, keeps asking until valid input is given.
while True:
    years = int(input("What is your age? "))
    if valid_number(years) == True:
        continue
    while valid_number(years) == False:
        print("Invalid Input; Please try again. ")
        years = int(input("Age: "))
    print("Thank you!")
    break
