# Example Mini-Project:
# THE MYSTICAL OCTOSPHERE! by Andrea Crain

# This game is based on a common toy. It is a 
# round black ball with a clear plastic window. 
# The ball is filled with murky blue liquid
# and you use it as a fortune teller. You ask 
# a yes-or-no question and shake the ball. There 
# is a white many-sided die inside with answers, 
# and when you stop shaking, one of the sides
# floats up and is readable against the window.

# Here is a sample of the kind of
# output this program should produce:
#
# Your question was... Will I get rich?
# You shake the mystical octosphere.
# The cloudy liquid swirls, and a reply comes into view...
# The mystical octosphere says... Probably yes.
# 
# Your question was... Are the Cubs going to win the World Series?
# You shake the mystical octosphere.
# The cloudy liquid swirls, and a reply comes into view...
# The mystical octosphere says... Probably not.
#

# Let's get started!

# Up here, before everything else, import the random module
import random
# Type the command to import the random module above this line
# and make sure it is not indented at all.

# Next, fill in code for the function number_to_fortune
# This is a helper function.
# It should take in a number and send back a string
# 
# The possible numbers are between 0 through 7 inclusive
# (that means 0, 1, 2, 3, 4, 5, 6, or 7)
# and each number should translate to a fortune
# that would be the answer to a yes or no question.
#
# My suggested fortunes are:
# 0 - Yes, for sure!
# 1 - Probably yes.
# 2 - Seems like yes...
# 3 - Definitely not!
# 4 - Probably not.
# 5 - I really doubt it...
# 6 - Not sure, check back later!
# 7 - I really can't tell
#
# If somehow the function gets a number other than those 8
# it should send back a string saying that
# something was wrong with the input.

def number_to_fortune(number):
    """Assumes number[0, 7]
        Returns a String"""
    if number == 0:
        return "Yes, for sure!"
    elif number == 1:
        return "Probably yes."
    elif number == 2:
        return "Seems like yes..."
    elif number == 3:
        return "Definitely not!"
    elif number == 4:
        return "Probably not."
    elif number == 5:
        return "I really doubt it..."
    elif number == 6:
        return "Not sure, check back later!"
    elif number == 7:
        return "I really can't tell"
    else:
        return "Something was wrong with the input"

    
# TEST SECTION...    
#print
#print number_to_fortune(0)
#print number_to_fortune(1)
#print number_to_fortune(2)
#print number_to_fortune(3)
#print number_to_fortune(4)
#print number_to_fortune(5)
#print number_to_fortune(6)
#print number_to_fortune(7)
#print number_to_fortune(19)
#print

def mystical_octosphere(question):
    
    print question   # Print a line including the original question to the console.
    print "You shake the mystical octosphere."

    answer_number = random.randrange(0, 7)  
    answer_fortune = number_to_fortune(answer_number)
    
    print "The cloudy liquid swirls, and a reply comes into view..."
    
    print "The mystical octosphere says...", answer_fortune
    print ""    

mystical_octosphere("Will I get rich?")
mystical_octosphere("Are the Cubs going to win the World Series?")