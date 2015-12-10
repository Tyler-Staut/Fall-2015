#Name: Matthew N. Bowen
#File Name: MatthewBowenLab14
#Date: 23 September 2015
#Description: Does various different things; a review
choice = 0
while choice == 0:
    print("It's time to play the game!\n") #This is the menu screen
    print("1. Absolute Value\n")
    print("2. Number Testing\n")
    print("3. Odd or Even?\n")
    print("4. Quit the program.")
    choice = int(input("Which would you like to do? ")) #Make the choice
    while choice == 1: #When choice is equal to 1, execute absolute value!
        print("\nWelcome to Absolute Value!")
        int1 = int(input("\nPlease enter a positive or negative integer: "))
        if int1 > 0:
            print("The absolute value of ", int1, "is", int1)
        elif int1 < 0:
            int2 = -int1
            print("The absolute value of ", int1, "is", int2)
        print("\nWould you like to go again?\n")
        choice = int(input("Type 1 to replay or 0 to return to menu. "))
        while (choice > 1 or choice < 0):
            choice = int(input("Input was wrong; Type 1 to replay or 0 to return to menu. "))
    while choice == 2: #When choice is equal to 2, execute Number Test!
        print("\nWelcome to Number Test!") 
        int3 = int(input("\nWrite an integer: "))
        if int3 > 20:
            print(int3, "is greater than 20.")
        elif int3 < 10:
            print(int3, "is less than 10.")
        else:
            print(int3, "is between 10 and 20.")
        print("\nWould you like to go again?\n")
        choice = int(input("Type 2 to replay or 0 to return to menu. "))
        while (choice > 2 or choice == 1 or choice < 0):
            choice = int(input("Input was wrong; Type 2 to replay or 0 to return to menu. "))
    while choice == 3: #When choice is equal to 3, execute Odd or Even!
        print("\nWelcome to Odd or Even!")
        int4 = int(input("\nWrite an integer: "))
        if int4 % 2 ==0:
            print(int4, "Is even.")
        else:
            print(int4, "Is odd.")
        print("\nWould you like to go again?\n")
        choice = int(input("Type 3 to replay or 0 to return to menu. "))
        while (choice > 3 or choice == 2 or choice == 1 or choice < 0):
            choice = int(input("Input was wrong; Type 3 to replay or 0 to return to menu. "))
    while choice == 4: #When choice is equal to 4, end the program!
        print("\nThank you for playing! Goodbye!")
        break
        