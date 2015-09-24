print("Welcome to the Open Cylinder Area Problem!\n") 
print("An open cylindrical container is to have the volume of 'x times pi' or (x)*pi")
print("where 'x' is equal to 'h'*'r^2', and where 'h' is the height and 'r' is the radius.\n")
print("Find the values of 'r' and 'h' that will minimize the surface area of the cylinder.\n")
x = int(input("Coefficient of pi: "))
print("Volume of the cylinder would be %d*pi." %x)

r = round((x)**(1/3), 5)
h = round((x)**(1/3), 5)

print("The value of 'r' that will minimize the volume would be ", r) 
print("The value of 'h' that will minimize the volume would be ", h)
print(" ")
print("Notice how the values of 'h' and 'r' are equal!")
