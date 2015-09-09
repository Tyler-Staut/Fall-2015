# IM DONT WITH THIS TONIGHT
#I CAN'T RESIST THAT DOUBLE MEAT!!


from math import *



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
print('\n')                 #Spaces put between text so I can read info better
print("Angle of A must be between", 
      (atan(W/Z))/pi ,"pi and", 
      (pi - atan(W/Z))/pi , "pi")    #Made this span multiple lines so I can read it better.
A = pi * float(input("Angle of A = pi * "))
S = float(W/tan(A))
L = float(Z-S)
T = float(sqrt(W**2 + S**2))

print('\n')                 #Spaces put between text so I can read info better
print("L = ", L)
print("S = ", S)
print('\n')                 #Spaces put between text so I can read info better
#-------------------------------------------------------

base = 0
height = 0
radius = 0

area_Square = 0
area_SemiCircle = 0
area_Triangle = 0

room_1_area = 0
room_2_area = 0
room_3_area = 0
room_3_area = 0

#-----------------MORE VARIABLES-------------------------

def Square(base, height):
    area_Square = base * height
    print("The Area is: ", int(area_Square))
    area_Square = area_Square                   #Tried to store variable but failed
    
def SemiCircle(radius):
    area_SemiCircle = (math.pi(radius**2))/4
    print("The Area is: ", int(area_Circe))
    area_SemiCircle = area_SemiCircle

def Triangle(base, height):
    area_Triangle = (base * height)/2
    print("The Area is: ", int(area_Triangle))
    area_Triangle = area_Triangle

#-------------ROOM & SIZE QUESTIONS-----------------------
print("What Shape do you want your 4 rooms to be?\n",
      "You Can Choose: Square, SemiCircle, or Triangle.\n")


                            #Code for setting room 1 to a variable
                            #INCOMPLETE
while True:
    room1 = str(input("What shape do you want Room 1 to be?\n"))
    if room1 in ('Square', 'SemiCircle', 'Triangle'):
        break
    else:
        print('Input was Wrong. Try Again.')

#-----
if room1 in ('Square', 'SemiCircle', 'Triangle'):
    if Square:
        base = float(input("Base: "))
        height = float(input("Height: "))
        Square(base, height)
        room_1_area = area_Square
    elif SemiCircle:
        radius = float(input("Radius: "))
        SemiCircle(radius)
        room_1_area = area_SemiCircle
    elif Triangle:
        base = float(input("Base: "))
        height = float(input("Height: "))
        Triangle(base, height)
        room_1_area = area_Triangle

#-----
       
while True:
    room2 = str(input("What shape do you want Room 2 to be?\n"))
    if room2 in ('Square', 'SemiCircle', 'Triangle'):
        break
    else:
        print('Input was Wrong. Try Again.')
        
#-----
if room2 in ('Square', 'SemiCircle', 'Triangle'):
    if Square:
        base = float(input("Base: "))
        height = float(input("Height: "))
        Square(base, height)
        room_2_area = area_Square
    elif SemiCircle:
        radius = float(input("Radius: "))
        SemiCircle(radius)
        room_2_area = area_SemiCircle
    elif Triangle:
        base = float(input("Base: "))
        height = float(input("Height: "))
        Triangle(base, height)
        room_2_area = area_Triangle
#-----
        
while True:
    room3 = str(input("What shape do you want Room 3 to be?\n"))
    if room3 in ('Square', 'SemiCircle', 'Triangle'):
        break
    else:
        print('Input was Wrong. Try Again.')
        
#-----
if room3 in ('Square', 'SemiCircle', 'Triangle'):
    if Square:
        base = float(input("Base: "))
        height = float(input("Height: "))
        Square(base, height)
        room_3_area = area_Square
    elif SemiCircle:
        radius = float(input("Radius: "))
        SemiCircle(radius)
        room_3_area = area_SemiCircle
    elif Triangle:
        base = float(input("Base: "))
        height = float(input("Height: "))
        Triangle(base, height)
        room_3_area = area_Triangle
#-----
        
while True:
    room4 = str(input("What shape do you want Room 4 to be?\n"))
    if room4 in ('Square', 'SemiCircle', 'Triangle'):
        break
    else:
        print('Input was Wrong. Try Again.')
        
#-----
if room4 in ('Square', 'SemiCircle', 'Triangle'):
    if Square:
        base = float(input("Base: "))
        height = float(input("Height: "))
        Square(base, height)
        room_4_area = area_Square
    elif SemiCircle:
        radius = float(input("Radius: "))
        SemiCircle(radius)
        room_4_area = area_SemiCircle
    elif Triangle:
        base = float(input("Base: "))
        height = float(input("Height: "))
        Triangle(base, height)
        room_4_area = area_Triangle
#-----


#--------------------------------------------------------


#----------------THIS IS GETTING CHANGED-----------------

total_rooms_area = room_1_area + room_2_area + room_3_area + room_4_area

print(total_rooms_area)

#---------------------------------------------------------
