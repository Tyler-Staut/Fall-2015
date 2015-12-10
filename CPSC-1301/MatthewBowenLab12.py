#Name: Matthew N. Bowen
#File Name: MatthewBowenLab12
#Date: 18 September 2015
#Description: Finds the average and letter grade, given 5 grades

grade1 = int(input("Grade 1:")) #Gets input for 1st grade
grade2 = int(input("Grade 2:")) #Gets input for 2nd grade
grade3 = int(input("Grade 3:")) #Gets input for 3rd grade
grade4 = int(input("Grade 4:")) #Gets input for 4th grade
grade5 = int(input("Grade 5:")) #Gets input for 5th grade

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