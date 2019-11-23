# implementation of card game - Memory

import simplegui
import random

# global variables
cardsDeck = list(range(0,8)) + list(range(0,8))
cardsDeckExposed = 16 * [True]
cardSize = [50, 100]

# helper function to initialize globals
def new_game():
    global cardsDeck, cardsDeckExposed
    cardsDeck = list(range(0,8)) + list(range(0,8))
    cardsDeckExposed = 16 * [True]
    random.shuffle(cardsDeck)

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for idx in range(len(cardsDeck)):
        if cardsDeckExposed[idx]:
            canvas.draw_text(str(cardsDeck[idx]), [(idx * cardSize[0] + cardSize[0] / 2), 60], 32, "White")
            
        


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric