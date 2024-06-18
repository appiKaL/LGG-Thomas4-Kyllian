from typing import List
from random import choice
import os

class Hangman:
    """
    A class to represent the Hangman game.

    Attributes:
    possible_words (List[str]): A list of possible words from which one word is randomly selected for the player to guess.
    word_to_find (List[str]): The word that the player needs to guess, chosen randomly from `possible_words`.
    lives (int): The number of lives the player has. The player loses a life for each incorrect guess.
    correctly_guessed_letters (List[str]): A list representing the correctly guessed letters of the word. Initially, this is a list of underscores (`_`), one for each letter in `word_to_find`.
    wrongly_guessed_letters (List[str]): A list of letters that the player has guessed incorrectly.
    turn_count (int): The number of turns that have been taken.
    error_count (int): The number of incorrect guesses that have been made.
    """

    def __init__(self):
        """
        Initializes a new game by setting up the word to guess, initializing the lives,
        and setting up tracking for correctly and incorrectly guessed letters, as well as the turn and error counts.
        """
        self.possible_words: List[str] = ["becode", "learning", "mathematics", "sessions", "artichaud", "cafard"]
        self.word_to_find: List[str] = list(choice(self.possible_words))
        self.lives: int = 5
        self.correctly_guessed_letters: List[str] = ["_" for _ in self.word_to_find]
        self.wrongly_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0
    
    def play(self) -> None:
        """
        Prompts the player to enter a letter. Checks if the input is valid (i.e., a single alphabetic character).
        If the guessed letter is in the word, it updates `correctly_guessed_letters` accordingly.
        If the guessed letter is not in the word, it adds the letter to `wrongly_guessed_letters`, increments the error count, and decreases the lives by one.
        Increments the turn count after each guess.
        """
        
        letter = input("Enter a letter! : ")
        while len(letter) != 1 or not letter.isalpha():
            letter = input("Enter a valid letter! : ")
        
        if letter in self.word_to_find:
            for j, i in enumerate(self.word_to_find):
                if letter == i:
                    self.correctly_guessed_letters[j] = i
        else:
            self.wrongly_guessed_letters.append(letter)
            self.error_count += 1
            self.lives -= 1

        self.turn_count += 1
    
    def start_game(self) -> None:
        """
        Begins the game loop. Continuously calls `play()` until the game is over
        (either the player has run out of lives or has correctly guessed the word).
        Prints the current state of the guessed letters, wrongly guessed letters,
        remaining lives, error count, and turn count after each guess.
        """
        

        while True:
            self.play()
            if self.lives == 0:
                self.game_over()
                break
            if self.correctly_guessed_letters == self.word_to_find:
                self.well_played()
                break
            os.system("clear") 
            print(self.correctly_guessed_letters)
            print(self.wrongly_guessed_letters)
            print(f"You have {self.lives} lives left, you have made {self.error_count} errors and it is the {self.turn_count} turn.")

    def game_over(self) -> None:
        """
        Prints a "Game Over" message. This method is called when the player has run out of lives.
        """
        print("  G A M E  O V E R !  ")

    def well_played(self) -> None:
        """
        Prints a congratulatory message showing the correctly guessed word, the number of turns taken, and the number of errors made.
        This method is called when the player has correctly guessed the word.
        """
        print(f"You found the word: {''.join(self.word_to_find)} in {self.turn_count} turns with {self.error_count} errors!")



