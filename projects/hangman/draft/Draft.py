from typing import List
import os

def get_word() -> str :
    word = input("Enter a word: ")
    return word

def get_lives() -> int :
    lives = input("Enter a number of lives: ")
    while not lives.isdigit():
        lives = input("Enter a number of lives: ")
    return int(lives)

def get_guess(suggested_letters: List[str]) -> List[str]:
    guess = input("Enter a letter:")
    while len(guess) != 1 or guess in suggested_letters == True or not guess.isalpha():
        guess = input("Enter a letter: ")
    suggested_letters.append(guess)
    return suggested_letters

def assess_guess(secret_word : str , guessed_letter : str , lives_left : int) -> int :
    if not guessed_letter in secret_word:
        lives_left -= 1
    return lives_left

def display_word(secret_word : str, suggested_letters : List[str]) -> bool :
    # char_list = [char_list.append("_") for _ in range(len(secret_word))]
    # for j, i in enumerate(secret_word):
    #     if i in suggested_letters:
    #         char_list[j] = i
    # print(char_list)
    # if "_" in char_list:
    #   return False
    # else:
    #   Return True
    os.system("clear")

    char_list = [i if i in suggested_letters else "_" for i in secret_word]
    print(char_list)
    return "_" in char_list

def main():

    os.system("clear")

    word: str = get_word()
    lives: int = get_lives()
    suggested_letters: List[str] =  []

    while display_word(word, suggested_letters) and lives > 0:
        print(f"You have {lives} left !")
        suggested_letters = get_guess(suggested_letters)
        lives = assess_guess(word, suggested_letters[-1], lives)
        
    if lives > 0:
        print("You found the word ! GG ")
    else:
        print("Losers will lose")
        
if __name__ == "__main__" : 
    main()