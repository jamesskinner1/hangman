# milestone_2.py

import random

# favorite fruits
favorite_fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
# Assign the list to the variable word_list
word_list = favorite_fruits
# Select a random word from the word_list
word = random.choice(word_list)

# Ask the user to enter a single letter and assign it to the variable guess
guess = input("Enter a single letter: ")

# single alphabetical character
if len(guess) == 1 and guess.isalpha():
    # If the check passes, print "Good guess!"
    print("Good guess!")
else:
    # If the check fails, print an error message
    print("Oops! That is not a valid input.")
