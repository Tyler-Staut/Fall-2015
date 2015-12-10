#Author: Tyler R. Staut
#File Name: TylerStautLab17.py
#Date: 9/30/2015
#Description: Counting with loops.

#-----STEP 1-----
print("Step 1:")
i = 20
while i > 0:        #It is converted now to a while loop
    print(i)
    i -= 2
#----------------

print('\n')     #Seperates the parts

#-----STEP 2-----
print("Step 2:")
for a in range(0, 101, 10):     #And now I converted to a for loop
    print(a, end=' ')
#----------------

print('\n')     #Seperates the parts

#-----STEP 3-----
print("Step 3:")
    
print('''The Answer to step 3 is: No, this loop cannot be converted to a while loop because it will not be able to take in negative 
numbers and will not be able to repeat. Some loops just were not meant to be for loops''') 
#----------------

print('\n')     #Seperates the steps

#-----STEP 4-----
print("Step 4:")        #I just used 3 for loops because putting it all in one would be too easy
for i in range(10):
    print('*', end=' ')
    
print('\n')

for i in range(5):
    print('*', end=' ')
    
print('\n')

for i in range(20):
    print('*', end=' ')
print('\n')
#----------------

print('\n')     #Seperates the steps

#-----STEP 5-----
print("Step 5:")
for i in range(10):     #Used range 10 twice to make the x and y axis of sorts for it to print
    for j in range(10):
        print('*', end=' ')
    print('\n')
#----------------

print("\n")     #Seperates the steps

#-----STEP 6-----
print("Step 6:")
for i in range(11):     #I didnt use range 10
    for j in range(i):  #Still pretty much the same as step 5 though
        print(j, end=' ')
    print('\n')
#----------------


