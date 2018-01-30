# Program 1:

# vals = [None]*10
# count = int(input("How many values should be stored in the array?"))
# while 1 < count < 9:
#     print("Value must be between 1 and 9.")
#     count = int(input("How many values should be stored in the array?"))
# for i in range(0, count):
#     vals[i] = count-i
# which = int(input("Which value do you wish to retrieve? "))
# while which > 9:
#     print("Value must be between 1 and 10.")
#     which = int(input("Which value do you wish to retrieve? "))
# print("Your value is", str(vals[which]))

#Program 2:

temps = [None]*10
numTemps = 0
count = 0
infile = open("temps.txt","r")           # open temps.txt file in read mode
for line in infile.readlines():          # Read each line from a file
    for i in line.split():              # Split each temperature from the line
        count += 1
        if count > 10:
            print("Index out of range.")
            break
        temps[numTemps] = float(i)      # assign each temperature to temps buffer
        numTemps += 1
    print(numTemps,"temperatures were read.")
