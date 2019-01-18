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

# helper functions

def name_to_number(name):
    if (name == "rock" or name == "Rock" or name == "ROCK"):
        return 0
    elif (name == "spock" or name == "Spock" or name == "SPOCK"):
        return 1
    elif (name == "paper" or name == "Paper" or name == "PAPER"):
        return 2
    elif (name == "lizard" or name == "Lizard" or name == "LIZARD"):
        return 3
    elif (name == "scissors" or name == "Scissors" or name == "SCISSORS"):
        return 4
    else:
        return "Error: your input does not match any of the five correct input strings"

def number_to_name(number):
    if (number == 0):
        return "rock"
    elif (number == 1):
        return "Spock"
    elif (number == 2):
        return "paper"
    elif (number == 3):
        return "lizard"
    elif (number == 4):
        return "scissors"
    else:
        return "Error: your input does not match any of the five correct input numbers"

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print ""
    
    # print out the message for the player's choice
    print "Player chooses", player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses", comp_choice
    
    # compute difference of comp_number and player_number modulo five
    result = (comp_number - player_number) % 5
    
    # use if/elif/else to determine winner, print winner message
    if (result == 1 or result == 2):
        print "Computer wins!"
    elif (result == 3 or result == 4):
        print "Player wins!"
    else:
        print "Player and computer tie!"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")