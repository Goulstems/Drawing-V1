import turtle
import time
from Color import Color

class DottedColor(Color):
    def _init_(self):
        super().__init__("BLUE",[0,0,255])
    def paintdottedline(self):
        for i in range (20):
            turtle.forward(5)
            turtle.penup()
            turtle.forward(5)
            turtle.pendown()


              

