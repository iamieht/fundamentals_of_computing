# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
num_range = 100
remainingGuesses = 7

# helper function to start and restart the game
def new_game():
    global secret_number, num_range, remainingGuesses, total_guesses
    secret_number = random.randrange(0, num_range)
    total_guesses = 0
    print "New game. Range is from 0 to", num_range
    print "Number of remaining guesses is", remainingGuesses



# define event handlers for control panel
def range100():
    global secret_number, num_range, remainingGuesses
    remainingGuesses = 7
    num_range = 100
    print ""
    new_game()

def range1000():
    global secret_number, num_range, remainingGuesses
    remainingGuesses = 10
    num_range = 1000
    print ""
    new_game()
    
def input_guess(guess):
    global remainingGuesses, total_guesses
    
    print ""
    print "Guess was", guess
    total_guesses += 1
    print "Number of remaining guesses is", remainingGuesses - total_guesses
    
    if total_guesses < remainingGuesses:
    
        if int(guess) > secret_number:
            print "Lower"
        elif int(guess) < secret_number:
            print "Higher"
        else:
            print "Correct!"
            print ""
            new_game()
    elif total_guesses == remainingGuesses:
        
        if guess == secret_number:
            print "Correct!\n"
            new_game()
                
        else:
            print "You ran out of remaining guesses. The number was", secret_number
            print ""
            new_game()    

    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements and start frame
frame.add_button("Range is[0,100)", range100)
frame.add_button("Range is[0,1000)", range1000)
frame.add_input("Type your guess:", input_guess, 50)


frame.start()

# call new_game 
new_game()

