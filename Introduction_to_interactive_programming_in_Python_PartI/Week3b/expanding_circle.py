# Expanding circle by timer

###################################################
# Student should add code where relevant to the following.

import simplegui 

WIDTH = 200
HEIGHT = 200
radius = 1


# Timer handler
def tick():
    global radius
    radius += 1

    
# Draw handler
def draw(canvas):
    canvas.draw_circle((HEIGHT / 2, WIDTH / 2), radius, 1, "Aqua", "Blue")

        
# Create frame and timer
frame = simplegui.create_frame("Expanding Circle", 200, 200)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)
frame.start()
# Start timer
timer.start()

