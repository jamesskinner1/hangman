import random
from milestone_2 import word_list
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
                    # Reduce the count of unique unguessed letters if this letter was not guessed before
                    if self.word_guessed.count(guess) == 1:
                        self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                if self.num_lives == 0 or self.num_letters == 0:
                    break

def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    print("Welcome to Hangman!")

    while True:
        if game.num_lives == 0:
            print("You lost!")
            print(f"The word was: {game.word}")
            break

        game.ask_for_input()

        if game.num_letters == 0:
            print(f"Congratulations! You won the game! The word was '{game.word}'.")
            break

# Example usage:
if __name__ == "__main__":
    word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    play_game(word_list)
