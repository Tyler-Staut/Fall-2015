#Authors: Tyler Staut - Matthew Bowen - Dean Debois
#File Name: MainProgramCPSC1-FirstProject.py
#Date: Oct 21, 2015
#Description: Program that will gather data from 3 files and calculate and display information from them.

#-----IMPORTS-----#
from operator import itemgetter
#-----------------#

#-----LISTS-----#

#---------------#

class MainFunctions():
    #LISTS
    ListOfCountries = []
    PopFemales1 = []
    PopMales1 = []
    PopFemales2 = []
    PopMales2 = []
    PopFemales3 = []
    PopMales3 = []
    
    TotalPopFemales = []
    TotalPopMales = []
    
    SortedByMales = []
    #LISTS
    SortedTop = []
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
        
    def openFile(self):
        #-----OPENS FILES-----#
        KidFile = open("WorldCensusAges0-14.csv")
        AdultFile = open("WorldCensusAges15-64.csv")
        SeniorFile = open("WorldCensusAges64+.csv")
        #---------------------#
    
    def closeFile(self):
        #-----CLOSES FILES-----#
        KidFile.close()
        AdultFile.close()
        SeniorFile.close()
        #----------------------#
        
    def createLists(self):
        #-----OPENS FILES-----#
        KidFile = open("WorldCensusAges0-14.csv")
        AdultFile = open("WorldCensusAges15-64.csv")
        SeniorFile = open("WorldCensusAges64+.csv")
        #---------------------#
        for line in KidFile:    #Sets up the lists
            fields = (line.split(","))
            T.ListOfCountries.append(fields[0].strip())
            T.PopMales1.append(fields[1].strip())
            T.PopFemales1.append(fields[2].strip())
        
        for line in AdultFile:
            fields = (line.split(","))
            T.PopMales2.append(fields[1].strip())
            T.PopFemales2.append(fields[2].strip())
            
        for line in SeniorFile:
            fields = (line.split(","))
            T.PopMales3.append(fields[1].strip())
            T.PopFemales3.append(fields[2].strip())
            
        for i in range(len(T.PopFemales1)):
            sum = int(T.PopFemales1[i])
            sum += int(T.PopFemales2[i])
            sum += int(T.PopFemales3[i])
            T.TotalPopFemales.append(sum)
            sum = 0
        
        for i in range(len(T.PopMales1)):
            sum = int(T.PopMales1[i])
            sum += int(T.PopMales2[i])
            sum += int(T.PopMales3[i])
            T.TotalPopMales.append(sum)
            sum = 0
        
        for i in range(len(T.TotalPopFemales)):
            sum = int(T.TotalPopFemales[i])
            sum += int(T.TotalPopMales[i])
            T.SortedTop.append(sum)
            sum = 0
          
        #-----------SORTED BY ALL------------#
        T.SortedAll = list(zip(T.ListOfCountries, T.TotalPopMales, T.TotalPopFemales))  
        #-----------SORTED BY MALES----------#
        T.SortedByMales = sorted(T.SortedAll, key=itemgetter(1))
        T.SortedByMales.reverse()
        #-----------SORTED BY TOP------------#
        T.SortedByTop = list(zip(T.ListOfCountries, T.SortedTop))
        T.SortedByTop = sorted(T.SortedByTop, key= itemgetter(1))
        T.SortedByTop.reverse()
        
        #-----CLOSES FILES-----#
        KidFile.close()
        AdultFile.close()
        SeniorFile.close()
        #----------------------#
        
    #------------------------------------------------------------------------------#

   
    def Option1(self):  #All countries with all population
        count = 0
        for country in range(len(T.ListOfCountries)):
            count += 1
            if ((count % 20) == 0) or (count == 0):
                print("#--------------------------------------------------------------#")
                print("# {:<28}      {:<15} {:<10} #".format("Country:", "Boys:", "Girls:"))
                print("#--------------------------------------------------------------#")
            print("  {:<28}      {:<15} {:<10}  ".format(T.ListOfCountries[country], T.TotalPopMales[country], T.TotalPopFemales[country]))
    
    def Option2(self):  #More Males than Females
        count = 0
        for country in range(len(T.SortedByMales)):
            count += 1
            if ((count % 20) == 0) or (count == 1):
                print("#--------------------------------------------------------------#")
                print("# {:<28}      {:<15} {:<10} #".format("Country:", "Boys:", "Girls:"))
                print("#--------------------------------------------------------------#")
            
            print("  {:<28}      {:<15} {:<10}  ".format(T.SortedByMales[country][0], T.SortedByMales[country][1], T.SortedByMales[country][2]))
            
    def Option3(self):  #Population by Letter
        count = 0
        Letter = input("What letter would you like to search for? ")
        Letter = Letter.upper()
        print("#--------------------------------------------------------------#")
        print("# {:<28}      {:<15} {:<10} #".format("Country:", "Boys:", "Girls:"))
        print("#--------------------------------------------------------------#")       
        for country in range(len(T.ListOfCountries)):
            count += 1
            if T.ListOfCountries[country][0] == Letter:
                print("  {:<28}      {:<15} {:<10}  ".format(T.SortedAll[country][0], T.SortedAll[country][1], T.SortedAll[country][2],))
                     
                     
    def Option4(self):  #Top 10 Countries with the most people
        print("#--------------------------------------------------------------#")
        print("# {:<28}      {:<15} {:<10} #".format("Country:", "Boys:", "Girls:"))
        print("#--------------------------------------------------------------#")       
        for country in range(10):
            if T.SortedByTop[country][0]:
                print("  {:<28}      {:<15}".format(T.SortedByTop[country][0], T.SortedByTop[country][1]))
    
    def Option5(self):  #Percentage of Old People
        OldPeople = []
        
        count1 = 0
        for x in range(len(T.ListOfCountries)):
            OldPeople.append(int(T.PopFemales3[x]) + int(T.PopMales3[x]))
        OldRatio = []
        for y in range(len(T.ListOfCountries)):
            OldRatio.append(int(OldPeople[y])/(int(T.PopFemales3[y]) + int(T.PopMales3[y]) + int(T.PopFemales2[y]) + int(T.PopMales2[y]) + int(T.PopFemales1[y]) + int(T.PopMales1[y])))
        for r in range (len(T.ListOfCountries)):
            OldRatio[r] = round(OldRatio[r]*100, 2)
        for z in range(len(T.ListOfCountries)):
            count1 += 1
            if ((count1 % 20) == 0) or (count1 == 0):
                print("#-----------------------------------------------------------------#")
                print("# {:<28}      {:<15} {:<10} #".format("Country:", "Total:", "Old People %:"))
                print("#-----------------------------------------------------------------#")
            print("  {:<28}      {:<15} {:<10}  ".format(T.SortedAll[z][0], (T.TotalPopFemales[z] + T.TotalPopMales[z]), OldRatio[z]))
    
    def Option6(self):  #Males to Females Percentage
        pass
    
    def Option7(self):  #Top 20 Countries with Least amount of Children
        Children = []
        LeastChildren = []
        print("#--------------------------------------------------------------#")
        print("# {:<28}      {:<15}  #".format("Country:", "Amount of Children"))
        print("#--------------------------------------------------------------#")
        for x in range(len(T.ListOfCountries)):
            Children.append(int(T.PopMales1[x]) + int(T.PopFemales1[x]))
        LeastChildren = list(zip(T.ListOfCountries, Children))
        LeastChildren = sorted(LeastChildren, key=itemgetter(1))
        
        for z in range(20):
            print("  {:<28}      {:<15} ".format(LeastChildren[z][0], LeastChildren[z][1]))
                    
    
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
T = MainFunctions() #Main Class of functions
#------------------------------------#


def menu():
    print("Choose an option that you want to view based on document.")
    
    print("Option 1: All Countries with All Population")    
    print("Option 2: More Males than Females")
    print("Option 3: Population by Letter")
    print("Option 4: Top 10 Countries with the most people")    #Sub option would determine which file to display
    print("Option 5: Percentage of Old People")
    print("Option 6: Males to Females Percentage")
    print("Option 7: Top 20 Countries with Least amount of Children")
    print("Option 8: Countries with similar Male to Female ratios")
    print("Option 9: Higher Female to Male ratio")
    print("Option 10: List all Data from File")
    print("Option 11: Quit Program")
    choice = int(input("Choose an Option: "))
    
    while choice not in range(1,12):
        choice = int(input("Choose an Option: "))
        
    if choice == 1:         #All Countries with All Population
        T.Option1()
    elif choice == 2:       #Tore Tales than Females
        T.Option2()
    elif choice == 3:       #Population by Letter
        T.Option3()
    elif choice == 4:       #Top 10 Countries with the most people
        T.Option4()
    elif choice == 5:       #Percentage of Old People
        T.Option5()
    elif choice == 6:       #Tales to Females Percentage
        T.Option6()
    elif choice == 7:       #Countries with Least amount of Children
        T.Option7()
    elif choice == 8:       #Countries with similar Tale to Female ratios
        T.Option8()
    elif choice == 9:       #Higher Female to Tale ratio
        T.Option9()
    elif choice == 10:      #List all Data from File
        T.Option10()
    elif choice == 11:      #Quit
        return 11
    
    

    
def main():
    start = 0
    T.createLists()
    while start != 11:
        start = menu()  #Keeps program going if not 11
        
        

main()

        
