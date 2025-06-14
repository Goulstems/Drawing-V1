#Import statements
from Color import Color
import turtle

#Turtle Components
screen = turtle.Screen()    #for input
canvas = screen.getcanvas() #for graphics

#Our objects of our custom `Color.py` class!
red = Color("RED",[255,0,0])
blue = Color("BLUE",[0,0,225])
green = Color("GREEN",[0,255,0])

#Keep track of keypresses
drawingState = {
    "Up": False,
    "Down": False,
    "Left": False,
    "Right": False
}

# - - - - - -- - - - - - - - - -- - - - - -- - - - - - - - - -- - - - - -- - - - - - - - - -
# Callbacks / Helper functions

# - - - - - - - - - - -- -  - -- - - - - - -
# [FOR DOWN PRESSING]
def callback_down_press(event=None):
    if not drawingState["Down"]:
        drawingState["Down"] = True
        draw_down_continuous()

def draw_down_continuous():
    if drawingState["Down"]:
        green.PAINTLINE(20, 270)
        screen.ontimer(draw_down_continuous, 50)  # slower repeat for visibility

def callback_down_release(event=None):
    drawingState["Down"] = False

canvas.bind("<KeyPress-Down>", callback_down_press)
canvas.bind("<KeyRelease-Down>", callback_down_release)
## - - - - - - - - - - -- -  - -- - - - - - -

canvas.focus_set()  # focus to receive key events

# Other turtle shortcuts
turtle.onkey(turtle.clear, "x")
turtle.onkey(turtle.down, "d")
turtle.onkey(turtle.up, "u")

# - - - - -- - - - - - - - - - - - - - - - - -
turtle.listen()
turtle.done()
