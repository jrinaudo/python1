# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

secret_number = 0
maxrange = 100
remaining_guesses = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, remaining_guesses
    secret_number = random.randrange(0, maxrange)
    remaining_guesses = int(math.ceil(math.log(maxrange + 1, 2)))
    print ""
    print "New game. Range is from 0 to", maxrange
    print "Number of remaining guesses is", remaining_guesses
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global maxrange
    maxrange = 100
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global maxrange
    maxrange = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global remaining_guesses
    remaining_guesses -= 1
    int_guess = int(guess)
    print ""
    print "Guess was", int_guess
    if (remaining_guesses > 0 and int_guess > secret_number):
        print "Number of remaining guesses is", remaining_guesses
        print "Lower!"
    elif (remaining_guesses > 0 and int_guess < secret_number):
        print "Number of remaining guesses is", remaining_guesses
        print "Higher!"
    elif (remaining_guesses == 0 and int_guess != secret_number):
        print "Sorry, you just lost the game. Please try again..."
        new_game()
    else:
        print "Correct!"
        new_game()
    
# create frame
frame = simplegui.create_frame('Guess the number', 200, 200)

# register event handlers for control elements and start frame
button100 = frame.add_button('Range is [0,100)', range100, 200)
button1000 = frame.add_button('Range is [0,1000)', range1000, 200)
guessbox = frame.add_input('Enter a guess', input_guess, 100)
frame.start()

# call new_game 
new_game()