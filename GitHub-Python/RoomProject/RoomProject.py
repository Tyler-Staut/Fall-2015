# IM DONT WITH THIS TONIGHT
#I CAN'T RESIST THAT DOUBLE MEAT!!


import math



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
      (math.atan(W/Z))/math.pi ,"pi and", 
      (math.pi - math.atan(W/Z))/math.pi , "pi")    #Made this span multiple lines so I can read it better.
A = math.pi * float(input("Angle of A = pi * "))
S = float(W/math.tan(A))
L = float(Z-S)
T = float(math.sqrt(W**2 + S**2))

print('\n')                 #Spaces put between text so I can read info better
print("L = ", L)
print("S = ", S)
print('\n')                 #Spaces put between text so I can read info better
#-------------------------------------------------------

base = 1
height = 1

#-----------------MORE VARIABLES-------------------------

def shape(Square):
    bace * height
    print("Square")
    
    
def shape(Semi_Circle):
    (math.pi(radius**2))/4
    print("Semi-Circle")

def shape(Triangle):
    (base * height)/2
    print("Triangle")

#------------------QUESTIONS-----------------------------
print("What Shape do you want your 4 rooms to be?\n",
      "You Can Choose: Square, Semi-Circle, or Triangle.\n")


                            #Code for setting room 1 to a variable
                            #INCOMPLETE
while True:
    room1 = input("What shape do you want Room 1 to be?\n")
    if room1 in ('Square', 'Semi-Circle', 'Triangle'):
        break
    else:
        print('Input was Wrong. Try Again.')


shape(room1)          #Needs to print variable from above but its not right now for some reason
print(room1)

#--------------------------------------------------------

#----------------THIS IS GETTING CHANGED-----------------

#room1 = W*Y
#room2 = (L*W)+((S*W)/2)
#room3 = X*Y
#room4 = X*Z

room_1_area = 1
room_2_area = 1
room_3_area = 1
room_4_area = 1


total_rooms_area = room_1_area + room_2_area + room_3_area + room_4_area

#---------------------------------------------------------
