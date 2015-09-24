import math
print("Welcome to the box problem!")
print("A rectangular box is made from a sheet of cardboard that is 'a' inches long,")
print("and 'b' inches wide by cutting a square from each corner and turning up the sides.\n")
print("'a' will equal the length of cardboard, 'b' the width of the cardboard,")
print("and with 'L' as the length of the side of the square to be cut from each corner.\n")
print("Find the volume of the largest box that can be constructed.\n")
a = float(input("Length of cardboard: a = "))
b = float(input("Width of cardboard: b = "))
A = 12
B = ((-4*a)-(4*b))
C = a*b
L1 = (-B + math.sqrt((B**2)-4*A*C))/24
L2 = (-B - math.sqrt((B**2)-4*A*C))/24
Volume1 = L1*a*b - 2*b*(L1**2) - 2*a*(L1**2) + 4*(L1**3)
Volume2 = L2*a*b - 2*b*(L2**2) - 2*a*(L2**2) + 4*(L2**3)
if Volume1 > Volume2:
    L = L1 
    Volume = Volume1
elif Volume2 > Volume1:
    L = L2
    Volume = Volume2

print("The length 'L' that will give you the maximum volume of the box is ", L )

print("The optimal volume of the box, given this value of L, is ", Volume)
