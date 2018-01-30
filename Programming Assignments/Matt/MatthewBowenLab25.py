#Name: Matthew Newton Bowen
#File Name: MatthewBowenLab25
#Date: 21 October 2015
#Description: File I/O

movieList1 = []   #creates the main lists
movieList2 = []
def getByRating(rating):     #Defines the function
    movieFile = open("C:\\file.txt")   #Opens the file
    for line in movieFile:
        fields = line.split(" ")   #Splits each line wherever there are spaces
        if int(fields[2]) > rating:  #If the rating of the movie is greater than the user input rating, it will add to a list.
            movieList1.append(fields[0].strip())
    movieFile.close() #Closes the file
    return movieList1 #Returns the list of films fitting the criteria

def getByYear(year): #Defines the function
    movieFile = open("C:\\file.txt")  #Opens the file
    for line in movieFile:
        fields = line.split(" ")  #Splits the line every time there's a space
        if int(fields[1]) > year: #If the year of the movie is greater than the user input year, it will add to a list.
            movieList2.append(fields[0].strip())
    movieFile.close() #Closes the file
    return movieList2 #Returns the list of films fitting the criteria

def main(): #Defines function
    rate = int(input("Enter a rating to search by (1-10): ")) #user Input rating
    print("Your results are: ") 
    length1 = len(getByRating(rate))
    for x in range(length1): #Prints out the components
        print(movieList1[x])
    year = int(input("Enter a year to search for movies that are newer than that year: "))
    print("Your results are: ")
    length2 = len(getByYear(year))
    for x in range(length2):
        print(movieList2[x])
    
main()
