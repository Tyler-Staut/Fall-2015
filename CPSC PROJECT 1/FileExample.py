#Authors: Tyler Staut - Matthew Bowen - Dean Debois
#File Name: FileExample.py
#Date: Oct 21, 2015
#Description: Example

#-----IMPORTS-----#

#-----------------#

#-----LISTS-----#



#---------------#

class ThatSecondWhenYouAreOnJohnCenasBackAndYouDontKnowIfHeIsGoingToDropYou():
    def Kid(self):
        myfile = open("WorldCensusAges0-14.csv")
        count = 0
        for line in myfile:
            count += 1
            fields = (line.split(","))
            if ((count % 10) == 0) or (count == 1):
                print("#-----------------------------------------------------------#")
                print("# {:<15} {:<15} {:<25} #".format("Boys:", "Girls:", "Country:"))
                print("#-----------------------------------------------------------#")
            print("{:<15} {:<15} {}".format(fields[1].strip(), fields[2].strip(), fields[0].strip()))
        myfile.close()
        
        
    def Adult(self):
        myfile = open("WorldCensusAges15-64.csv")
        count = 0
        for line in myfile:
            count += 1
            fields = (line.split(","))
            if ((count % 10) == 0) or (count == 1):
                print("#-----------------------------------------------------------#")
                print("# {:<15} {:<15} {:<25} #".format("Boys:", "Girls:", "Country:"))
                print("#-----------------------------------------------------------#")
            print("{:<15} {:<15} {}".format(fields[1].strip(), fields[2].strip(), fields[0].strip()))
        myfile.close()
        
        
    def Senior(self):
        myfile = open("WorldCensusAges64+.csv")
        count = 0
        for line in myfile:
            count += 1
            fields = (line.split(","))
            if ((count % 10) == 0) or (count == 1):
                print("#-----------------------------------------------------------#")
                print("# {:<15} {:<15} {:<25} #".format("Boys:", "Girls:", "Country:"))
                print("#-----------------------------------------------------------#")
            print("{:<15} {:<15} {}".format(fields[1].strip(), fields[2].strip(), fields[0].strip()))
        myfile.close()
        
T = ThatSecondWhenYouAreOnJohnCenasBackAndYouDontKnowIfHeIsGoingToDropYou()


def menu():
    print("Choose an option that you want to view based on document.")
    
    print("Option 1: Top 10 Countries with the most people")    #Sub option would determine which file to display
    print("Option 2: Percentage of Old People")
    print("Option 3: Males to Females Percentage")
    print("Option 4: Countries with Least amount of Children")
    print("Option 5: Countries with similar Male to Female ratios")
    print("Option 6: Higher Males to Females and Higher Females to Males")
    print("Option 7: List all Data from File")
    choice = int(input("Choose an Option: "))
    
    while choice not in range(1,8):
        choice = int(input("Choose an Option: "))
        
    if choice == 1:         #Top 10 Countries with the most people
        pass
    elif choice == 2:       #Percentage of Old People
        pass
    elif choice == 3:       #Males to Females Percentage
        pass
    elif choice == 4:       #Countries with Least amount of Children
        pass
    elif choice == 5:       #Countries with similar Male to Female ratios
        pass
    elif choice == 6:       #Higher Males to Females and Higher Females to Males
        pass
    elif choice == 7:       #List all Data from File
        allData()
    
    
def allData():      #Moving over to menu definition so that the code will work better.
    print("Choose an age range.")
    print("1: Ages 0-14")
    print("2: Ages 15-64")
    print("3: Ages 64+")
    choice = int(input("Choose an Option: "))
    while choice not in (1,2,3):
        choice = int(input("Choose an Option: "))
        
    if choice == 1:
        T.Kid()
    elif choice == 2:
        T.Adult()
    elif choice == 3:
        T.Senior()
    
def main():  
    start = 0
    
    while start != 8:
        menu()
        
        
        
    
    
    
main()

        
