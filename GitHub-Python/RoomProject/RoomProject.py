# IM DONT WITH THIS TONIGHT
#I CAN'T RESIST THAT DOUBLE MEAT!!


from math import *



#------------------PLACE HOLDER----------------------
#
#print('''\n                 ----L--------/ \n
#        |          |    \       /\n
#      W |     1    |  2  \T    /\n
#        |          |     /\   /\n
#        ----------------/--A\/ \n  ''')
#print('''          
#        |          |        |\n
#      X |    3     |    4   |\n
#        |          |        |\n
#        -----Y----------Z----\n''')
#
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
    area_Square = float(base * height)
    print("The Area is: ", float(area_Square))
                       #Tried to store variable but failed
    
def SemiCircle(radius):
    area_SemiCircle = float((pi(radius)**2)/4)
    print("The Area is: ", float(area_SemiCircle))
    

def Triangle(base, height):
    area_Triangle = float((base * height)/2)
    print("The Area is: ", float(area_Triangle))
    

#-------------ROOM & SIZE QUESTIONS-----------------------
print("What Shape do you want your 4 rooms to be?\n",
      "You Can Choose: Square, SemiCircle, or Triangle.\n")



while True:
    room1 = str(input("What shape do you want Room 1 to be?\n"))
    if room1 in ('Square', 'SemiCircle', 'Triangle'):
        if room1 == 'Square':
            base = float(input("Base: "))
            height = float(input("Height: "))
            Square(base, height)
            room_1_area = area_Square
        elif room1 == 'SemiCircle':
            radius = float(input("Radius: "))
            SemiCircle(radius)
            room_1_area = area_SemiCircle
        elif room1 == 'Triangle':
            base = float(input("Base: "))
            height = float(input("Height: "))
            Triangle(base, height)
            room_1_area = area_Triangle
        break
    else:
        print('Input was Wrong. Try Again.')

#-----

#-----
       
while True:
    room2 = str(input("What shape do you want Room 2 to be?\n"))
    if room2 in ('Square', 'SemiCircle', 'Triangle'):
        if room2 == 'Square':
            base = float(input("Base: "))
            height = float(input("Height: "))
            Square(base, height)
            room_2_area = area_Square
        elif room2 == 'SemiCircle':
            radius = float(input("Radius: "))
            SemiCircle(radius)
            room_2_area = area_SemiCircle
        elif room2 == 'Triangle':
            base = float(input("Base: "))
            height = float(input("Height: "))
            Triangle(base, height)
            room_2_area = area_Triangle
        break
    else:
        print('Input was Wrong. Try Again.')
#-----

#-----
        
while True:
    room3 = str(input("What shape do you want Room 1 to be?\n"))
    if room3 in ('Square', 'SemiCircle', 'Triangle'):
        if room3 == 'Square':
            base = float(input("Base: "))
            height = float(input("Height: "))
            Square(base, height)
            room_3_area = area_Square
        elif room3 == 'SemiCircle':
            radius = float(input("Radius: "))
            SemiCircle(radius)
            room_3_area = area_SemiCircle
        elif room3 == 'Triangle':
            base = float(input("Base: "))
            height = float(input("Height: "))
            Triangle(base, height)
            room_3_area = area_Triangle
        break
    else:
        print('Input was Wrong. Try Again.')
        
#-----

#-----
        
while True:
    room4 = str(input("What shape do you want Room 4 to be?\n"))
    if room4 in ('Square', 'SemiCircle', 'Triangle'):
        if room4 == 'Square':
            base = float(input("Base: "))
            height = float(input("Height: "))
            Square(base, height)
            room_4_area = area_Square
        elif room4 == 'SemiCircle':
            radius = float(input("Radius: "))
            SemiCircle(radius)
            room_4_area = area_SemiCircle
        elif room4 == 'Triangle':
            base = float(input("Base: "))
            height = float(input("Height: "))
            Triangle(base, height)
            room_4_area = area_Triangle
        break
    else:
        print('Input was Wrong. Try Again.')
        


#--------------------------------------------------------


#----------------THIS IS GETTING CHANGED-----------------

total_rooms_area = room_1_area + room_2_area + room_3_area + room_4_area

print(total_rooms_area)

#---------------------------------------------------------
