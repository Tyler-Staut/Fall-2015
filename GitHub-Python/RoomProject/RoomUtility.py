'''
Created on Sep 10, 2015

@author: Tyler
'''

from math import *

#Used to define what the Square room area is
def squareRoom(base, height):
    area = base * height
    
#Used to define what the SemiCircle room area is    
def semicircleRoom(radius):
    area = (pi(radius)**2) / 4
    
#Used to define what the Triangle room area is    
def triangleRoom(base, height):
    area = (base * height) / 2 
    
#Used to define the first room
def room1():
    room_1_area = area
