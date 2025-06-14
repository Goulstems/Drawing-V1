import turtle
import time
from tkinter import *
def getColor(RGB):
    r=RGB[0]
    g=RGB[1]
    b=RGB[2]
    return (r,g,b)
class Color:
    def __init__(self, name, RGB):
        self.name = name
        self.RGB = RGB
    def PAINTLINE(self,dist,dir):
        turtle.colormode(255)
        turtle.setheading(dir)
        turtle.pencolor(getColor(self.RGB))
        turtle.forward(dist)
    def PAINTCIRCLE(self):
        turtle.pencolor(getColor(self.RGB))
        turtle.circle(80)
        turtle.forward(80)
    def PAINTTRIANGLE(self):
            turtle.pencolor(getColor(self.RGB))
            for i in range (3):
                turtle.forward(100)
                turtle.left(120)   
    def PAINTSQUARE(self):
            turtle.pencolor(getColor(self.RGB))
            turtle.right(120)
            turtle.forward(160)
            turtle.right(120)
            turtle.forward(160)
            turtle.right(120)
            turtle.forward(160)
            turtle.right(120)
            turtle.forward(320)
    
    
        
        
        
    
    
    
