# Rock-paper-scissors-lizard-Spock template

import random
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
#print (4 - 4) % 5 
# 1 & 2 wins / 3 & 4 looses / 0 tied
# helper functions

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
   

def rpsls(player_choice):

    print ""                                            # print a blank line to separate consecutive games
    print "Player chooses", player_choice               # print out the message for the player's choice
    player_number = name_to_number(player_choice)       # convert the player's choice to player_number using the function name_to_number()
    comp_number = random.randrange(0, 4)                # compute random guess for comp_number using random.randrange()
    comp_choice = number_to_name(comp_number)           # convert comp_number to comp_choice using the function number_to_name()
    print "Computer chooses", comp_choice               # print out the message for computer's choice

    if type(comp_number) == int and type(player_number) == int: # compute difference of comp_number and player_number modulo five
        difference = (comp_number - player_number) % 5

        if difference == 1 or difference == 2:
            print "Computer wins!"
        elif difference == 3 or difference == 4:
            print "Player wins!"
        else:
            print "Player and computer tie!"
    else:
        print "Invalid option"


    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
rpsls("perro")



