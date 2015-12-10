# Program 1:

vals = [None]*10
count = int(input("How many values should be stored in the array?"))
for i in range(0, count):
  vals[i] = count-i
which = int(input("Which value do you wish to retrieve? "))
print("Your value is", str(vals[which]))

#Program 2:

'''temps = [None]*10
numTemps = 0
infile = open("temps.txt","r")           
for line in infile.readlines():          
    for i in line.split(): 
        if numTemps >= 10:
            print("Number of Temps exceeded, stopping program.")
            break
        temps[numTemps] = float(i)  
        numTemps += 1
    print(numTemps,"temperatures were read.")'''
