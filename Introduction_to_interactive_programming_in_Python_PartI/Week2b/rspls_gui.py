# GUI-based version of RPSLS

###################################################
# Student should add code where relevant to the following.

import simplegui
import random

# Functions that compute RPSLS
def name_to_number(name):
    """Assumes name is String
        Returns an Int[0, 4]"""
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return "Invalid input"

def number_to_name(number):
    """Assumes number is an Int[0, 4]
        Returns a String"""
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return 'Invalid Input'

def rspls(guess):
    player_number = name_to_number(guess)		        		# convert the player's choice to player_number using the function name_to_number() 
    comp_number = random.randrange(0, 4)                		# compute random guess for comp_number using random.randrange()
    comp_choice = number_to_name(comp_number)           		# convert comp_number to comp_choice using the function number_to_name()
    print "Computer chooses", comp_choice               		# print out the message for computer's choice
    if type(comp_number) == int and type(player_number) == int: # compute difference of comp_number and player_number modulo five
        difference = (comp_number - player_number) % 5
        
        if difference == 1 or difference == 2:
            print "Computer wins!"
        elif difference == 3 or difference == 4:
            print "Player wins!"
        else:
            print "Player and computer tie!"
            
    else:
        print "Error: Bad input " + guess + " to rpsls"
    
# Handler for input field
def get_guess(guess):
    if guess not in ('Spock', 'rock', 'paper', 'lizard', 'scissors'):
        print "Error: Bad input " + guess + " to rpsls"
        print ""
    else:
        print "Player chooses", guess
        rspls(guess)
        print ""
    


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#
