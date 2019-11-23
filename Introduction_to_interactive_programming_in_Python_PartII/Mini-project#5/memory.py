# implementation of card game - Memory

import simplegui
import random

# Global Variables
turns = 0 

# helper function to initialize globals
def new_game():
    '''
    Start of the game
    '''
    global memory_deck, exposed, state, turns
    state = 0 # -> Number of cards exposed
    turns = 0
    label.set_text("Turns = " + str(turns))
    memory_deck = range(0,8) + range(0,8)
    random.shuffle(memory_deck)
    exposed = [False] * 16 # List: True-> Card Exposed / False-> Not exposed


     
# define event handlers
def mouseclick(pos):
    '''
    Main Game Logic
    '''
    global exposed, state, card1_idx, card2_idx, turns

    # index of the clicked card
    idx = pos[0] // 50
    
    # flip cards depending on the state
    if state == 0:
        
        exposed[idx] = True
        card1_idx = idx
        state = 1
        
    elif state == 1:
        
        if not exposed[idx]:
            exposed[idx] = True
            card2_idx = idx
            turns += 1 # Increase the turns when the first card is flipped
            
            state = 2        
            label.set_text("Turns = " + str(turns))
              
    elif state == 2:
        
        if not exposed[idx]:
            exposed[idx] = True
            
            if not memory_deck[card1_idx] == memory_deck[card2_idx]:
                exposed[card1_idx] = False
                exposed[card2_idx] = False
                
            card1_idx = idx
                                        
            state = 1 
    
                            
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed, turns

    for card in range(1, 17):
        if exposed[card - 1]:
            # Horizontal location
            horz = (card * 50) - 35            
            canvas.draw_text(str(memory_deck[card - 1]), [horz, 65], 48, "White")
        else:
            # Rectangle points
            a = (card * 50) - 50
            b = 0
            c = card * 50
            d = 100
            canvas.draw_polygon([(a, b), (a, d), (c, d), (c, b)], 2, "Black", "Green")
        


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