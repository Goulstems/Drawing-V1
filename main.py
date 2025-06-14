from Color import Color
from Red import Red
from Blue import Blue
import turtle
import time
from DottedLine import DottedColor
red = Color("RED",[255,0,0])
blue = Color("BLUE",[0,0,225])
green = Color("GREEN",[0,255,0])
def callbackx1():
    green.PAINTLINE(20,0)
def callbacky1():
    green.PAINTLINE(20,90)
def callbackx2():
    green.PAINTLINE(20,180)
def callbacky2():
    green.PAINTLINE(20,270)
turtle.speed(10)
turtle.onkey(callbackx1,"Right")
turtle.onkey(callbacky1,"Up")
turtle.onkey(callbackx2,"Left")
turtle.onkey(callbacky2,"Down")
turtle.onkey(turtle.clear,"x")
turtle.onkey(turtle.down,"d")
turtle.onkey(turtle.up,"u")
turtle.listen()


