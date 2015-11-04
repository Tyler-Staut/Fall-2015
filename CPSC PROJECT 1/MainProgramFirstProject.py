#Authors: Tyler Staut - Matthew Bowen - Dean Debois
#File Name: MainProgramCPSC1-FirstProject.py
#Date: Oct 21, 2015
#Description: Program that will gather data from 3 files and calculate and display information from them.

#-----IMPORTS-----#

#-----------------#

#-----LISTS-----#
ListOfCountries = []
TotalPopFemales = []
TotalPopMales = []
#---------------#

class SpecificFileData():
    def Kid(self):
        myfile = open("WorldCensusAges0-14.csv")
        count = 0
        for line in myfile:
            count += 1
            fields = (line.split(","))
            if ((count % 20) == 0) or (count == 1):
                print("#--------------------------------------------------------------#")
                print("# {:<28}      {:<15} {:<10} #".format("Country:", "Boys:", "Girls:"))
                print("#--------------------------------------------------------------#")
            print("  {:<28}      {:<15} {:<10}  ".format(fields[0].strip(), fields[1].strip(), fields[2].strip()))
        myfile.close()
        
        
    def Adult(self):
        myfile = open("WorldCensusAges15-64.csv")
        count = 0
        for line in myfile:
            count += 1
            fields = (line.split(","))
            if ((count % 20) == 0) or (count == 1):
                print("#--------------------------------------------------------------#")
                print("# {:<28}      {:<15} {:<10} #".format("Country:", "Boys:", "Girls:"))
                print("#--------------------------------------------------------------#")
            print("  {:<28}      {:<15} {:<10}  ".format(fields[0].strip(), fields[1].strip(), fields[2].strip()))
        myfile.close()
        
        
    def Senior(self):
        myfile = open("WorldCensusAges64+.csv")
        count = 0
        for line in myfile:
            count += 1
            fields = (line.split(","))
            if ((count % 20) == 0) or (count == 0):
                print("#--------------------------------------------------------------#")
                print("# {:<28}      {:<15} {:<10} #".format("Country:", "Boys:", "Girls:"))
                print("#--------------------------------------------------------------#")
            print("  {:<28}      {:<15} {:<10}  ".format(fields[0].strip(), fields[1].strip(), fields[2].strip()))
        myfile.close()
        
    #------------------------------------------------------------------------------#

class MainFunctions():    
    def Option1(self):  #All countries with all population
        ListOfCountries = []
        PopFemales1 = []
        PopMales1 = []
        PopFemales2 = []
        PopMales2 = []
        PopFemales3 = []
        PopMales3 = []
        
        TotalPopFemales = []
        TotalPopMales = []
        #-----OPENS FILES-----#
        KidFile = open("WorldCensusAges0-14.csv")
        AdultFile = open("WorldCensusAges15-64.csv")
        SeniorFile = open("WorldCensusAges64+.csv")
        #---------------------#
        for line in KidFile:    #Sets up the lists
            fields = (line.split(","))
            ListOfCountries.append(fields[0].strip())
            PopMales1.append(fields[1].strip())
            PopFemales1.append(fields[2].strip())
        
        for line in AdultFile:
            fields = (line.split(","))
            PopMales2.append(fields[1].strip())
            PopFemales2.append(fields[2].strip())
            
        for line in SeniorFile:
            fields = (line.split(","))
            PopMales3.append(fields[1].strip())
            PopFemales3.append(fields[2].strip())
            
        for amount in PopFemales1:
            TotalPopFemales.append(PopFemales1[amount].slice()+PopFemales2[amount].slice()+PopFemales3[amount].slice())
        
        for amount in PopMales1:
            TotalPopMales.append(PopMales1[amount].slice()+PopMales2[amount].slice()+PopMales3[amount].slice())
        
        print(TotalPopFemales)
        
        KidFile.close()
        AdultFile.close()
        SeniorFile.close()
                
    
    def Option2(self):  #More Males than Females
        pass
    
    def Option3(self):  #Population by Letter
        pass
     
    def Option4(self):  #Top 10 Countries with the most people
        pass
    
    def Option5(self):  #Percentage of Old People
        pass
    
    def Option6(self):  #Males to Females Percentage
        pass
    
    def Option7(self):  #Countries with Least amount of Children
        pass
    
    def Option8(self):  #Countries with similar Male to Female ratios
        pass
    
    def Option9(self):  #Higher Female to Male ratio
        pass
    
    def Option10(self): #List all data from Specific file
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
        #------------------------------------------------------------------------------#
        
#----------CLASS ASSIGNMENT----------#
T = SpecificFileData() #First Class
M = MainFunctions() #Main Class of functions
#------------------------------------#


def menu():
    print("Choose an option that you want to view based on document.")
    
    print("Option 1: All Countries with All Population")    
    print("Option 2: More Males than Females")
    print("Option 3: Population by Letter")
    print("Option 4: Top 10 Countries with the most people")    #Sub option would determine which file to display
    print("Option 5: Percentage of Old People")
    print("Option 6: Males to Females Percentage")
    print("Option 7: Countries with Least amount of Children")
    print("Option 8: Countries with similar Male to Female ratios")
    print("Option 9: Higher Female to Male ratio")
    print("Option 10: List all Data from File")
    print("Option 11: Quit Program")
    choice = int(input("Choose an Option: "))
    
    while choice not in range(1,12):
        choice = int(input("Choose an Option: "))
        
    if choice == 1:         #All Countries with All Population
        M.Option1()
    elif choice == 2:       #More Males than Females
        M.Option2()
    elif choice == 3:       #Population by Letter
        M.Option3()
    elif choice == 4:       #Top 10 Countries with the most people
        M.Option4()
    elif choice == 5:       #Percentage of Old People
        M.Option5()
    elif choice == 6:       #Males to Females Percentage
        M.Option6()
    elif choice == 7:       #Countries with Least amount of Children
        M.Option7()
    elif choice == 8:       #Countries with similar Male to Female ratios
        M.Option8()
    elif choice == 9:       #Higher Female to Male ratio
        M.Option9()
    elif choice == 10:      #List all Data from File
        M.Option10()
    elif choice == 11:      #Quit
        return 11
    
    

    
def main():
    start = 0
    
    while start != 11:
        start = menu()  #Keeps program going if not 11
        
        

main()

        
