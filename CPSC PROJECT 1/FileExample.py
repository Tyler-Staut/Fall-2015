#Author: Tyler R. Staut
#File Name: FileExample.py
#Date: Oct 21, 2015
#Description: Example

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
        
        
    def JohnCena(self):
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
    print("Choose an option that you want to view.")
    
    print("Option 1: Top 10 Countries with the most people")    #Sub option would determine which file to display
    print("Option 2: Percentage of Old People")
    print("Option 3: Males to Females Percentage")
    print("Option 4: Countries with Least amount of Children")
    print("Option 5: Countries with similar Male to Female ratios")
    print("Option 6: ")
    print("Option 7: List all Data from File")
    choice = int(input("Choose an Option: "))
    
    
    
def subMenu():
    print("Choose an age range.")
    print("1: Ages 0-14")
    print("2: Ages 15-64")
    print("3: Ages 64+")
    choice = int(input("Choose an Option: "))
    
def main():
    x = menu()
    y = subMenu()
    
    
    
    
main()

        
