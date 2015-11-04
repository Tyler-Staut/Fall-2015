#Authors: Tyler Staut - Matthew Bowen - Dean Debois
#File Name: MainProgramCPSC1-FirstProject.py
#Date: Oct 21, 2015
#Description: Example

#-----IMPORTS-----#

#-----------------#

#-----LISTS-----#



#---------------#

class ComputerScienceOne_MWF_10AM():
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
        
    def Top10WithMostPeople(self):
        pass
    
    def PercentageOldGeezers(self):
        pass
    
    def MaleToFemaleXLRcable(self):
        pass
    
    def NoChildren(self):
        pass
    
    def SameMaleFemale(self):
        pass
    
    def MoreOfOneOrAnother(self):
        pass
    
    def allData(self):      #Moving over to menu definition so that the code will work better.
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
        
T = ComputerScienceOne_MWF_10AM()


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
    choice = int(input("Choose an Option: "))
    
    while choice not in range(1,12):
        choice = int(input("Choose an Option: "))
        
    if choice == 1:         #All Countries with All Population
        pass
    elif choice == 2:       #More Males than Females
        pass
    elif choice == 3:       #Population by Letter
        pass
    elif choice == 4:       #Top 10 Countries with the most people
        pass
    elif choice == 5:       #Percentage of Old People
        pass
    elif choice == 6:       #Males to Females Percentage
        pass
    elif choice == 7:       #Countries with Least amount of Children
        pass
    elif choice == 8:       #Countries with similar Male to Female ratios
        pass
    elif choice == 9:       #Higher Female to Male ratio
        pass
    elif choice == 10:      #List all Data from File
        T.allData()
    elif choice == 11:      #Quit
        break
    
    

    
def main():  
    start = 0
    
    while start != 8:
        menu()
        
        

main()

        
