#Author: Tyler R. Staut
#File Name: TylerStautLab25.py
#Date: Oct 21, 2015
#Description: Lists and using filesystem

#-----LISTS-----#
rating = []
year = []
#---------------#

#----------DEFINITIONS----------#
def getByRating(usr_rating):
    movieFile = open("file.txt")    #Opens file
    
    for line in movieFile:
        fields = line.split(" ")    #Splits parts of file
        
        if int(fields[2]) > (usr_rating):
            rating.append(fields[0].strip())    #Appends to list
    movieFile.close()   #Closes file
    return rating   #Returns rating
        

def getByYear(usr_year):
    movieFile = open("file.txt")    #Opens file
    
    for line in movieFile:
        fields = line.split(" ")    #Seperates parts of file
        
        if int(fields[1]) > (usr_year): #Compares to input
            year.append(fields[0].strip())
    movieFile.close()   #Closes file
    return year #Returns year

def main():     #Main Function
    x = int(input("Enter a rating to search movies (1-10): "))  #Get user rating
    print("Your Results Are: ")
    amount1 = len(getByRating(x))
    for i in range(amount1):
        print(rating[i])    #Prints movies above rating
        
    print('\n')
    y = int(input("Enter a year to search movies (1955-2015): "))   #Gets user year
    print("Your Results Are: ")
    amount2 = len(getByYear(y))
    for t in range(amount2):
        print(year[t])  #Prints movies above year


#-------------------------------#

#-----PROGRAM-----#
main()      #Starts Program
#-----------------#
