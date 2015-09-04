import math
import bacon


#------------------PLACE HOLDER----------------------
print('''\n                 ----L--------/ \n
        |          |    \       /\n
      W |     1    |  2  \T    /\n
        |          |     /\   /\n
        ----------------/--A\/ \n  ''')
print('''          
        |          |        |\n
      X |    3     |    4   |\n
        |          |        |\n
        -----Y----------Z----\n''')

#----------------------------------------------------
#--------------------BASE CODE-----------------------

W = float(input("W= "))
X = float(input("X= "))
Y = float(input("Y= "))
Z = float(input("Z= "))
print("Angle of A must be between", (math.atan(W/Z))/math.pi ,"pi and", (math.pi - math.atan(W/Z))/math.pi , "pi")
A = math.pi * float(input("Angle of A = pi * "))
S = float(W/math.tan(A))
L = float(Z-S)
T = float(math.sqrt(W**2 + S**2))
print("L = ", L)
print("S = ", S)

room1 = W*Y
room2 = (L*W)+((S*W)/2)
room3 = X*Y
room4 = X*Z

totalarea = room1 + room2 + room3 + room4

print(totalarea)
