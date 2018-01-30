myfile = open("C:\\NameOfFile.txt") #Put the file location before the file name. Use double slashes.

lastnames = []
firstnames = []

for line in myfile:
    fields = line.split(",") 
    lastnames.append(fields[0].split()) #does just last names
    firstnames.append(fields[1].split()) #does just first names
    #print(fields[1].strip(), fields[0].strip())
myfile.close()