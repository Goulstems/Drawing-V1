from Color import Color
import turtle

screen = turtle.Screen()    #for input
canvas = screen.getcanvas() #for graphics

drawingState = {
    "Up": False,
    "Down": False,
    "Left": False,
    "Right": False
}

green = Color("GREEN",[0,255,0])

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

canvas.focus_set()  # focus to receive key events