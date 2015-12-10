#Name: Matthew N. Bowen
#File Name: MatthewBowenLab13
#Date: 21 September 2015
#Description: Finds the average and letter grade, given 5 grades, and does a loop
go = 1
while go == 1:
    grade1 = int(input("Grade 1:")) #Gets input for 1st grade
    while grade1 > 100 or grade1 < 0: #Makes it so that grade must be between 0 and 100
        grade1 = int(input("Grade not valid; enter a grade between 0 and 100: "))
    grade2 = int(input("Grade 2:")) #Gets input for 2nd grade
    while grade2 > 100 or grade2 < 0: 
        grade2 = int(input("Grade not valid; enter a grade between 0 and 100: "))
    grade3 = int(input("Grade 3:")) #Gets input for 3rd grade
    while grade3 > 100 or grade3 < 0:
        grade3 = int(input("Grade not valid; enter a grade between 0 and 100: "))
    grade4 = int(input("Grade 4:")) #Gets input for 4th grade
    while grade4 > 100 or grade4 < 0:
        grade4 = int(input("Grade not valid; enter a grade between 0 and 100: "))
    grade5 = int(input("Grade 5:")) #Gets input for 5th grade
    while grade5 > 100 or grade5 < 0: #Makes it so that grade must be between 0 and 100
        grade5 = int(input("Grade not valid; enter a grade between 0 and 100: "))
    
    average = float((grade1 + grade2 + grade3 + grade4 + grade5)/5) #computes the average of the 5 grades
    
    print("Your Numeric Average is", average) #Prints the actual numeric grade
    
    if 90 <= average <=100: #If average is between 90 and 100, you make an A
        print("Your Letter Grade is an A")
    elif 80 <= average <= 89: #If average is between 80 and 89, you make a B
        print("Your Letter Grade is a B")
    elif 70 <= average <= 79: #If average is between 70 and 79, you make a C
        print("Your Letter Grade is a C")
    elif 65 <= average <= 69: #If average is between 65 and 69, you make a D
        print("Your Letter Grade is a D")
    elif 0 <= average <= 64: #If average is between 0 and 64, you make an F
        print("Your Letter Grade is a F")
    go = int(input("Would you like to continue? 1= yes 0= no. ")) #Makes it so you may end the loop if you wish
print("Bye!")   #End

