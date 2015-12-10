#Name: Matthew N. Bowen
#File Name: MatthewBowenLab11
#Date: 16 September 2015
#Description: Finds the best deal on boxes of cereal


print("Welcome to the product chooser!") # Intro

cereal1 = input("Please enter the name of the first product: ") # Gets name of first cereal
price1 = float(input("Please enter the price of the first product: $"))# Gets price of first cereal
size1 = float(input("Please enter the size of the first product (in ounces): ")) # Gets size of first cereal in ounces
ratio1 = price1/size1 # Gets price per ounce
print("\n") # New Line

cereal2 = input("Please enter the name of the second product: ") # Gets name of second cereal
price2 = float(input("Please enter the price of the second product: $")) # Gets price of second cereal
size2 = float(input("Please enter the size of the second product (in ounces): ")) # Gets size of second cereal in ounces
ratio2 = price2/size2 # Gets price per ounce
print("\n") # New Line

cereal3 = input("Please enter the name of the third product: ") # Gets name of third cereal
price3 = float(input("Please enter the price of the third product: $")) # Gets price of third cereal
size3 = float(input("Please enter the size of the third product (in ounces): ")) # Gets size of third cereal in ounces
ratio3 = price3/size3 # Gets price per ounce
print("\n") #New Line

if ratio2 > ratio1 < ratio3: #If ratio 2 is less than ratio 1 and 3, then that cereal is the best deal
    best = cereal1
    print(best, "is the best value! Enjoy your Breakfast!" )
elif  ratio1 > ratio2 < ratio3: #If ratio 2 is less than ratio 1 and 3, then that cereal is the best deal
    best = cereal2
    print(best, "is the best value! Enjoy your Breakfast!" )
else: # Otherwise, cereal 3 must be the best deal
    best = cereal3
    print(best, "is the best value! Enjoy your Breakfast!")
    
