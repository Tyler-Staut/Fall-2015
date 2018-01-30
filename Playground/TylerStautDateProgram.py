#Description: Program that displays the date a user enters in a new format.
#Author: Tyler Staut
#Date: Wed Sep 20

from datetime import date

#----------Month and Day Names----------#
monthName = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#---------------------------------------#

#----------Date Initialization----------#
d = date.today() #This is just to give it an initial value
#---------------------------------------#

#----------Functions----------#
def input(): #Function that gets user input to do other functions
    while True: #Infinite loop
        try:
            date = raw_input("Input: ") #Gets user input
            if(date.lower() == "q"):
                exit() #Quits program

            month, day, year = date.split("/") #Splits up the date. If date does not fit in this tuple it is wrong

            month = month.lstrip('0') #Gets rid of leading 0's
            day = day.lstrip('0') #Gets rid of leading 0's

            #print(month + "/" + day + "/" + year) This was for debugging
            print("") #Prints a new Line

            if(checkDate(month, day, year) == True): #This checks the date
                printDate(month, day, year) #So we can print it
            else:
                continue #Otherwise it is wrong and needs to be fixed
        except Exception: #This exception tells the user that what they did is wrong and they need to fix it
            print("Data entered is incorrect.")
            print("Format must be MM/DD/YYYY or M/D/YYYY")
            continue #So the user can put input in again

def checkDate(month, day, year): #Function that checks the date
    #Converts the month day and year into integers so the date function does not get upset
    month = int(month)
    day = int(day)
    year = int(year)
    while True: #Infinite loop
        try:
            d = date(year, month, day) #This got upset with string values because I forgot to make the month, day and year integers
        except ValueError as e:
            print(e) #This is not the greatest but it tells the user what was bad with the date
            return False #This is so the user can put in another date but hopefully correctly
        return True #This is to say the date checks out


def printDate(month, day, year): #Function that prints out the date
    month = int(month) #This is used to get the month name

    #Prints out month name, day and year and says what day of the week it is
    print(monthName[month-1] + " " + day + ", " + year + " is a " + daysOfWeek[d.weekday()])
    print("") #Prints a new Line

def main(): #Main function
    while True: #loop to continually get input
        input() #Calls input function
#-----------------------------#

#Calls main function
main()
