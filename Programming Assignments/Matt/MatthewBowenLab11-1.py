#Name: Matthew N. Bowen
#File Name: MatthewBowenLab11
#Date: 16 September 2015
#Description: Finds the best deal on boxes of cereal


print("Welcome to the product chooser!")

cereal1 = input("Please enter the name of the first product: ")
price1 = float(input("Please enter the price of the first product: $"))
size1 = float(input("Please enter the size of the first product (in ounces): "))
ratio1 = price1/size1
print("\n")

cereal2 = input("Please enter the name of the second product: ")
price2 = float(input("Please enter the price of the second product: $"))
size2 = float(input("Please enter the size of the second product (in ounces): "))
ratio2 = price2/size2
print("\n")

cereal3 = input("Please enter the name of the third product: ")
price3 = float(input("Please enter the price of the third product: $"))
size3 = float(input("Please enter the size of the third product (in ounces): "))
ratio3 = price3/size3
print("\n")

if ratio2 > ratio1 < ratio3:
    best = cereal1
    if ratio2 < ratio3:
        middle = cereal2
        worst = cereal3
    else:
        middle = cereal3
        worst = cereal2
    print(best, "is the best value" )
    print(middle, "is the second best value.")
    print(worst, "is the worst value." )
elif  ratio1 > ratio2 < ratio3:
    best = cereal2
    if ratio1 < ratio3:
        middle = cereal1
        worst = cereal3
    else:
        middle = cereal3
        worst = cereal1
    print(best, "is the best value" )
    print(middle, "is the second best value.")
    print(worst, "is the worst value." )
elif ratio2 > ratio3 < ratio1:
    best = cereal3
    if ratio1 < ratio2:
        middle = cereal1
        worst = cereal2
    else:
        middle = cereal2
        worst = cereal1
    print(best, "is the best value" )
    print(middle, "is the second best value.")
    print(worst, "is the worst value." )

