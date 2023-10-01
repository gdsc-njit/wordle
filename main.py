import random
import sys
from termcolor import colored

def menuPrint():
    print("PLAY WORDLE")

def getRandomWord():
    with open("dictionary.txt") as file:
        words = file.read().splitlines()
        return random.choice(words)

def gameBegin():
    print("Type a 5-letter word and hit ENTER")
    word = getRandomWord()
    for attempt in range(6):
        guess = input().lower()

        while len(guess) != 5:
            print("5-letter please: ", end="")
            guess = input().lower()
        
        for i in range(5):
            if guess[i] == word[i]:
                print(colored(guess[i], "black", "on_green"), end="")
            elif guess[i] in word:
                print(colored(guess[i], "black", "on_light_yellow"), end="")
            else:
                print(guess[i], end="")

        if guess == word:
            print(colored("\nCORRECT. Congratulations!", "green"))
            return
        else:
            print()
    print(colored(f"WRONG. The answer is {word}!", "red"))

# main    
menuPrint()

stillPlay = ""
while stillPlay != "N" and stillPlay != "n":
    gameBegin()
    stillPlay = input("Hit ENTER to continue. Type N or n to quit.")
