# Echo mouse click in console

###################################################
# Student should enter code below
import simplegui

def click(position):
    print position


# create frame
frame = simplegui.create_frame("Echo clicks", 200, 200)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)

# start frame
frame.start()




###################################################
# Sample output

#Mouse click at (104, 105)
#Mouse click at (169, 175)
#Mouse click at (197, 135)
#Mouse click at (176, 111)
#Mouse click at (121, 101)
#Mouse click at (166, 208)
#Mouse click at (257, 235)
#Mouse click at (255, 235)