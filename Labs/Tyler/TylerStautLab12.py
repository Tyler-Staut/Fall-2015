#Author: Tyler R. Staut
#File Name: TylerStautLab12
#Date: 9/18/2015
#Description: Grade calculator.

#Grade List
grade = []

#-----NUM OF ASSIGNMENTS------
numAssignments = 5  #Could be changed if needed to be expanded later on
#-----------------------------

#----------INTRO----------
print("Welcome to the Auto Grader!")
print("Grade percent entered must be between 0.0 and 100.")
#-------------------------

#----------DEFINITIONS----------
def letterGrade(grade):     #Determines the Letter grade
    if 90 <= grade <= 100:
        letterGrade = 'A'
        return letterGrade
    elif 80 <= grade <= 89:
        letterGrade = 'B'
        return letterGrade
    elif 70 <= grade <= 79:
        letterGrade = 'C'
        return letterGrade
    elif 65 <= grade <= 69:
        letterGrade = 'D'
        return letterGrade
    elif 0 <= grade <= 64:
        letterGrade = 'F'
        return letterGrade
#-------------------------------
 

 
#----------INPUTS----------
def runProgram():
    x = 1   #Used for the grade # entered
    while x <= 5:
        userGrade = float(input("Enter grade %d: " % x))
        if (0 <= userGrade <= 100):
            grade.append(userGrade)
            x = x + 1 
        else:
            print("Try again.")
  
#--------------------------
runProgram()
#----------GRADE CALCULATOR----------
grade = float(sum(grade)/5) #Used 5 because I got lazy and did'nt remember off the top of my head how to count amount in list


letterGrade = str(letterGrade(grade))   #Calls for letter grade
#------------------------------------

#----------OUTPUT----------
print("Your average grade is %d which is an %s." % (grade, letterGrade))
#--------------------------