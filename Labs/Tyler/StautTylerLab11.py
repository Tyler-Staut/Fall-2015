#Author: Tyler R. Staut
#File Name: StautTylerLab11.py
#Date: 9/16/2015
#Description: Finds the best deal between 3 boxes of cereal

#----------Welcome Message----------
print("Welcome to the product chooser!")
#-----------------------------------

#----------LISTS TO STORE INFO IN----------
productName = []
productPrice = []
productOunces = []
totalAmount = []
#------------------------------------------

#----------DEFINITIONS----------
def cereal():
    name = input("Please enter the name of the first product: ")
    productName.append(name)    #Puts the Name you entered in the Name list
    
    price = round(float(input("Please enter the price of the first product: ")), 2)
    productPrice.append(price)  #Puts the price you entered in the Price list
    
    amount = int(input("Please enter the size of the first product: "))
    productOunces.append(amount)    #Puts the size you put in the Ounces list
#-------------------------------------------------

#----------------RUN CEREAL-----------------  
cereal()    #Runs the program for the first time to get the first set of data.
cereal()    #Runs the program again to get the next set of data.
cereal()    #Runs the program again to get the last set of data.
#-------------------------------------------

#Used to find the total price of the cereal you buy if you get a certain amount
for i in range(0, len(productName)):    #Used to get an answer and store the values in the totalAmount list
    totalAmount.append(productPrice[i] / productOunces[i])

#Used to sort the name data with respect to the total amount data
totalAmount, productName = zip(*sorted(zip(totalAmount, productName)))

#----------OUTPUT----------
print("The best deal is ", productName[0], "Enjoy your breakfast!!!")
#--------------------------