# Example Mini-Project:
# THE MYSTICAL OCTOSPHERE! - Andrea Crain

# Type-your-question version

# Before starting this practice mini-project,
# make sure you've done the week 1 version of the
# Mystical Octosphere. In that version, you had to
# enter your questions into the code at the bottom.

# In week 2 of the class, though, we want to allow
# people to enter their question into an input
# box. It will still display the output in the
# console and use all the same logic as last week.

# Believe it or not, we can do this by adding just 
# three lines of code!

# Let's get started!

# In addition to the random module, we also need to import
# the simplegui module now. That's the library that
# can make a window pop up with an input box.
import random

import simplegui
# Type the command to import the simplegui module above this line
# and make sure it is not indented at all.

# You do not need to change the function number_to_fortune
def number_to_fortune(number):
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
        return "I really can't tell."
    else:
        return "Something was wrong with my input."

# You do not need to change the main function either!
def mystical_octosphere(question):
    print "Your question was... " + question
    print "You shake the mystical octosphere."
    answer_number = random.randrange(0, 8)
    answer_fortune = number_to_fortune(answer_number)
    print "The cloudy liquid swirls, and a reply comes into view..."
    print "The mystical octosphere says... " + answer_fortune    
    print
    

# Create frame
frame = simplegui.create_frame("GUI-based Mystical Octosphere", 50, 100)

# Now add an input field to the frame you made.
frame.add_input("What is your question?", mystical_octosphere, 200)

# Start frame
frame.start()
