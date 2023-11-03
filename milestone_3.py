# milestone_3.py

import random

# Define the list of fruits and select a random one as the secret word
favorite_fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
word = random.choice(favorite_fruits).lower()

def check_guess(guess):
    # Step 2: Convert the guess into lower case
    guess = guess.lower()
    
    # Step 3: Check if the guess is in the word
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        # Ask the user for their guess
        guess = input("Guess a letter: ")
        
        # Check if the guess is a single alphabetic character
        if len(guess) == 1 and guess.isalpha():
            # Step 3: Call the check_guess function to check if the guess is in the word
            check_guess(guess)
            break  # Break out of the loop if the guess is valid
        else:
            # Inform the user if their input is not a valid single letter
            print("Invalid letter. Please, enter a single alphabetical character.")

# Step 4: Outside the function, call the ask_for_input function to test your code
ask_for_input()
