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

area_Square1 = 0
area_SemiCircle1 = 0
area_Triangle1 = 0

area_Square2 = 0
area_SemiCircle2 = 0
area_Triangle2 = 0

area_Square3 = 0
area_SemiCircle3 = 0
area_Triangle3 = 0

area_Square4 = 0
area_SemiCircle4 = 0
area_Triangle4 = 0

room_1_area = 0
room_2_area = 0
room_3_area = 0
room_3_area = 0

#-----------------MORE VARIABLES-------------------------

def Square(base, height):
    area_Square = float(base * height)
    print("The Area is: ", float(area_Square))
    area_Square = area_Square

    
def SemiCircle(radius):
    area_SemiCircle = (pi(radius)**2)/4
    print("The Area is: ", float(area_SemiCircle))
    area_SemiCircle = area_SemiCircle
    

def Triangle(base, height):
    area_Triangle = float((base * height)/2)
    print("The Area is: ", float(area_Triangle))
    area_Triangle = area_Triangle
    

def roomArea(area_Square, area_SemiCircle, area_Triangle):
    area_of_room = area_Square + area_SemiCircle + area_Triangle
    
    
def room1(area_of_room):

    

    

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
        elif room1 == 'SemiCircle':
            radius = float(input("Radius: "))
            SemiCircle(radius)
        elif room1 == 'Triangle':
            base = float(input("Base: "))
            height = float(input("Height: "))
            Triangle(base, height)
        roomArea(area_Square1, area_SemiCircle1, area_Triangle1)
        break
    else:
        print('Input was Wrong. Try Again.')



#--------------------------------------------------------


#----------------THIS IS GETTING CHANGED-----------------

total_rooms_area = room_1_area
'''
total_rooms_area = (roomArea(area_Square1, area_SemiCircle1, area_Triangle1) 
                    + roomArea(room_2_area = area_Square2 + area_SemiCircle2 + area_Triangle2) 
                    + roomArea(room_3_area = area_Square3 + area_SemiCircle3 + area_Triangle3) 
                    + roomArea(room_4_area = area_Square4 + area_SemiCircle4 + area_Triangle4))

'''
print(total_rooms_area)

#---------------------------------------------------------
