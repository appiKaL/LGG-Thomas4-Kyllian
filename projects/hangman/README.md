# Hangman Game

![Berserk hanging tree](https://i.makeagif.com/media/8-31-2023/fTCusP.gif)

This is a Python implementation of the classic Hangman game. The game selects a word at random from a predefined list of possible words, and the player has to guess the word by suggesting letters within a certain number of guesses.

## How to Play

1. The game will randomly select a word from the list of possible words.
2. You need to guess the word by entering one letter at a time.
3. If the guessed letter is in the word, it will be revealed in its correct position(s).
4. If the guessed letter is not in the word, you will lose one life.
5. The game continues until you either guess the word correctly or run out of lives.

## Features

- Randomly selects a word from a list of possible words.
- Tracks correctly and incorrectly guessed letters.
- Provides feedback on the number of lives remaining and the number of incorrect guesses.
- Clears the console screen after each turn for a clean interface.
- Displays a congratulatory message when the word is guessed correctly.
- Displays a game over message when the player runs out of lives.

## Installation

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. Clone the repository or download the code files to your local machine.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where you have saved the code files.
3. Run the game by executing the following command:

    ```bash
    python hangman.py
    ```

4. Follow the on-screen prompts to play the game.

## Code Overview

### Class: `Hangman`

#### Attributes

- `possible_words` (List[str]): A list of possible words from which one word is randomly selected for the player to guess.
- `word_to_find` (List[str]): The word that the player needs to guess, chosen randomly from `possible_words`.
- `lives` (int): The number of lives the player has. The player loses a life for each incorrect guess.
- `correctly_guessed_letters` (List[str]): A list representing the correctly guessed letters of the word. Initially, this is a list of underscores (`_`), one for each letter in `word_to_find`.
- `wrongly_guessed_letters` (List[str]): A list of letters that the player has guessed incorrectly.
- `turn_count` (int): The number of turns that have been taken.
- `error_count` (int): The number of incorrect guesses that have been made.

#### Methods

- `__init__(self)`: Initializes a new game by setting up the word to guess, initializing the lives, and setting up tracking for correctly and incorrectly guessed letters, as well as the turn and error counts.
- `play(self)`: Prompts the player to enter a letter. Checks if the input is valid (i.e., a single alphabetic character). If the guessed letter is in the word, it updates `correctly_guessed_letters` accordingly. If the guessed letter is not in the word, it adds the letter to `wrongly_guessed_letters`, increments the error count, and decreases the lives by one. Increments the turn count after each guess.
- `start_game(self)`: Begins the game loop. Continuously calls `play()` until the game is over (either the player has run out of lives or has correctly guessed the word). Prints the current state of the guessed letters, wrongly guessed letters, remaining lives, error count, and turn count after each guess.
- `game_over(self)`: Prints a "Game Over" message. This method is called when the player has run out of lives.
- `well_played(self)`: Prints a congratulatory message showing the correctly guessed word, the number of turns taken, and the number of errors made. This method is called when the player has correctly guessed the word.

ENJOY !
