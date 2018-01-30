'''
Created on Sep 3, 2015

@author: Tyler
'''


def room():
    room = str(input("What shape do you want room " + roomnum + " to be.\n")
    if room in ('Square', 'SemiCircle', 'Triangle'):
        if room == 'Square':               #This is for Square room
            base = float(input("Base: "))
            height = float(input("Height: "))
            area = squareRoom(base, height)
            return area
            
        elif room == 'SemiCircle':         #This is for Semi-SemiCircle room
            radius = float(input("Radius: "))
            area = semicircleRoom(radius)
            return area
        elif room == 'Triangle':           #This is for triangle room
            base = float(input("Base: "))
            height = float(input("Height: "))
            area = triangleRoom(base, height)
            return area
        break
    else:
        print('Input was Wrong. Try Again.')
        
def room():
    room = str(input("What shape do you want room " + roomnum + " to be.\n"))
    if room in ('Square', 'SemiCircle', 'Triangle'):
        if room == 'Square':               #This is for Square room
                    base = float(input("Base: "))
                    height = float(input("Height: "))
                    area = squareRoom(base, height)
                    return area
                    
                elif room == 'SemiCircle':         #This is for Semi-SemiCircle room
                    radius = float(input("Radius: "))
                    area = semicircleRoom(radius)
                    return area
                elif room == 'Triangle':           #This is for triangle room
                    base = float(input("Base: "))
                    height = float(input("Height: "))
                    area = triangleRoom(base, height)
                    return area
                break
            else:
                print('Input was Wrong. Try Again.')