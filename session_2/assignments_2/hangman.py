'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''

# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''

"""
In this implementation, we first define a list of words to choose from and randomly select a word from the list. We then initialize a list called correct_guesses to keep track of the correct guesses (initially, it contains one underscore for each letter in the word). We also initialize a list called incorrect_guesses to keep track of the incorrect guesses (initially, it is empty). We set the maximum number of tries to 6.

We define a function called print_game_state to print the current game state (number of tries left, used letters, and the current state of the word). We then start the game by printing a welcome message and the initial game state.

We create a while loop that will run until the game is over. Inside the loop, we ask the user to guess a letter. We check if the guess is a single letter, if it has already been used, and if it is correct. If the guess is correct, we update the correct_guesses list to reflect the new letter(s) that have been guessed, and print a message indicating that the guess was correct. If all letters have been guessed, we print a message indicating that the word has been guessed correctly and break out of the loop.

If the guess is incorrect, we add it to the incorrect_guesses list and print a message indicating that the guess was incorrect. If the number of incorrect guesses is equal to or greater than the maximum number of tries, we print a message indicating that the game is over and break out of the loop.

Finally, we print the final game state (either the correct word or the word with some letters left to guess).
"""

import random

# Define a list of words to choose from
words = ['python', 'java', 'javascript', 'ruby', 'php']

# Choose a random word from the list
word = random.choice(words)

# Initialize a list to keep track of the correct guesses
correct_guesses = ['_' for _ in range(len(word))]

# Initialize a list to keep track of the incorrect guesses
incorrect_guesses = []

# Set the number of maximum tries
max_tries = 6

# Define a function to print the current game state
def print_game_state():
    print(f"You have {max_tries - len(incorrect_guesses)} tries left.")
    print("Used letters:", ' '.join(incorrect_guesses))
    print("Word:", ' '.join(correct_guesses))

# Start the game
print("Welcome to Hangman!")
print_game_state()

while True:
    # Ask the user to guess a letter
    guess = input("Guess a letter: ")

    # Check if the guess is a single letter
    if len(guess) != 1:
        print("Please enter a single letter!")
        continue

    # Check if the guess has already been used
    if guess in incorrect_guesses or guess in correct_guesses:
        print("You've already guessed that letter!")
        continue

    # Check if the guess is correct
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                correct_guesses[i] = guess
        print("Correct!")
        print_game_state()
        if '_' not in correct_guesses:
            print(f"You guessed the word {word}!")
            break
    else:
        incorrect_guesses.append(guess)
        print("Incorrect!")
        print_game_state()
        if len(incorrect_guesses) >= max_tries:
            print(f"You ran out of tries! The word was {word}.")
            break
