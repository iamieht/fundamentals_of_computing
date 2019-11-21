# Image positioning problem

###################################################
# Student should enter code below

import simplegui

# global constants
WIDTH = 400
HEIGHT = 300

# load test image
test_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid.png")
test_image_size = [95, 93]
test_image_center = [test_image_size[0] / 2, test_image_size[1] / 2]
image_pos = [WIDTH / 2, HEIGHT / 2]

# mouseclick handler
def click(pos):
    global image_pos
    image_pos = pos

    
# draw handler
def draw(canvas):
    global image_pos
    canvas.draw_image(test_image, test_image_center, test_image_size, 
                      image_pos, test_image_size)

    
# create frame and register draw handler    
frame = simplegui.create_frame("Test image", WIDTH, HEIGHT)
frame.set_canvas_background("Gray")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

# start frame
frame.start()
        
                                       