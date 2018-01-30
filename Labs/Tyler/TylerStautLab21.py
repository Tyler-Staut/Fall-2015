#Author: Tyler R. Staut
#File Name: TylerStautLab21.py
#Date: 10/12/2015
#Description: Does things similar to the magic 8 ball but is really the magical 9 ball
#-----IMPORTS-----
import random
#-----------------

#-----INTRO-----
print("Hi, and welcome to the Magic 9 ball! Ask a yes or no question and get a response. When you are done asking questions, enter (end)")
#---------------

#----------MAGIC 9 BALL----------
def Magic(number):
    #Positive output
    if number == 1:
        print("As I see it, yes")
    elif number == 2:
        print("Of course")
    elif number == 3:
        print("Without a doubt")
    #Negative output
    elif number == 4:
        print("I'm surprised you even asked, but no")
    elif number == 5:
        print("Why would you ever ask that, no, don't you ever say that again")
    elif number == 6:
        print("The Gods are displeased, they say no")
    #Neutral output
    elif number == 7:
        print("I cannot tell you now")
    elif number == 8:
        print("Please try again later, I'm sleeping")
    elif number == 9:
        print("My office hours begin at 3:00 PM Sharp EST")
        
#--------------------------------

#----------MAIN----------       
def main():
    number = -1
    while number != 0:
        ans = input("\nAsk me a question and I will choose your fate: ")
        if ans.lower() == 'end':
            break
        number = random.randint(1,9)
        Magic(number)
#------------------------
main()  #Launches Program    
        