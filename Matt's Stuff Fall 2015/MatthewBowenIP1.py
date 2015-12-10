#Name: Matthew N. Bowen
#Date: 25 September, 2015
#Title: MatthewBowenIP1 (Independent Programming 1)
#Purpose: Baggage Price Calculator


choice = "yes" #Begins the loop
while choice == "yes":
    name = input("What is your name? ") #Takes input of name
    number = int(input("How many bags do you need to check in? ")) #Takes input of number
    print(" ")
    while number < 0: #Eliminates possibility of negative input values 
        number = int(input("Please input a valid number. "))
    if number == 0: #States $0 for no baggage
        price = 0
    elif number == 1: #States $25 for 1 bag
        price = 25
    elif number > 1: #Calculates price for quantities over 1 bag
        price = 60 + (number-2)*50
    print("You will pay $%d on your baggage today.\n" %price) #States price
    print("Bon Voyage, %s!" %name) #Outputs name
    choice = input("Would you like to use this tool again? (yes/no) ") #User may exit loop or use again
print("Thank you for using the baggage fee calculator!") #Goodbye.

    