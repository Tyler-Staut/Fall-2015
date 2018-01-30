#Author: Tyler R. Staut
#File Name: TylerStautLab12
#Date: 9/18/2015
#Description: Grade calculator.



#----------INTRO----------
print("Welcome to the Auto Grader!")
print("Grade percent entered must be between 0.0 and 100.\n")
#-------------------------



#-------PROGRAM---------
start = 1       #Used so that the program will end later if user decides to
while start == 1:
    g1 = int(input("Enter grade #1: "))     #Input for grade
    while (g1 < 0) or (g1 > 100):   #Prevents user from inputing invalid input
        g1 = int(input("Input was wrong, try again: ")) #Input for grade if wrong
    
        
    g2 = int(input("Enter grade #2: "))
    while (g2 < 0) or (g2 > 100):
        g1 = int(input("Input was wrong, try again: "))
    
    g3 = int(input("Enter grade #3: "))
    while (g3 < 0) or (g3 > 100):
        g1 = int(input("Input was wrong, try again: "))
    
    g4 = int(input("Enter grade #4: "))
    while (g4 < 0) or (g4 > 100):
        g1 = int(input("Input was wrong, try again: "))
    
    g5 = int(input("Enter grade #5: "))
    while (g5 < 0) or (g5 > 100):
        g1 = int(input("Input was wrong, try again: "))
    
    
    grade = (g1 + g2 + g3 + g4 + g5) / 5        #Calculates number grade to find letter grade
    
    #----------LETTER GRADE MAKER----------
    if 90 <= grade <= 100:
        letterGrade = 'A'
        
    elif 80 <= grade <= 89:
        letterGrade = 'B'
        
    elif 70 <= grade <= 79:
        letterGrade = 'C'
        
    elif 65 <= grade <= 69:
        letterGrade = 'D'
        
    elif 0 <= grade <= 64:
        letterGrade = 'F'
    #--------------------------------------
    
    #----------OUTPUT----------
    print("\nYour average grade is %d which is an %s." % (grade, letterGrade))
    #--------------------------
    
    #----------PROGRAM RESTART OR QUIT----------
    print("\nWould you like to run the program again?")
    start = int(input("Enter 1 for yes and 0 to quit: "))
    #-------------------------------------------
print("Have a nice day.")       #End
