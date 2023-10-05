from wordle import Wordle
import random
from termcolor import colored

def loadWordSet(path: str):
    word_set = set()
    with open(path, "r") as file:
        for line in file.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set

def getRandomWord(wordset):
    return random.choice(list(wordset))

def drawBorder(lines, size=9, pad=1):
    content_length = size + pad * 2
    top_border = "┌" + "─" * content_length + "┐"
    bottom_border = "└" + "─" * content_length + "┘"
    space = " " * pad
    print(top_border)
    for line in lines:
        print("│" + space + line + space + "│")
    print(bottom_border)

def convertWord2Color(result):
    result_color = []
    for letter in result:
        if letter.in_right_position:
            backgr = "on_green"
        elif letter.in_word:
            backgr = "on_light_yellow"
        else:
            backgr = "on_red"
        colored_letter = colored(letter.character, "black", backgr)
        result_color.append(colored_letter)
    return " ".join(result_color)

def displayResult(wordle: Wordle):
    print(f"You have {wordle.remainingAttempts()} attempts left.")

    lines = []
    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convertWord2Color(result)
        lines.append(colored_result_str)

    for _ in range(wordle.remainingAttempts()):
        lines.append(" ".join(["_"] * wordle.WORD_LENGTH)) # - - - - - -

    drawBorder(lines)

def main():
    word_set = loadWordSet("src/dictionary.txt")
    word = getRandomWord(word_set)
    wordle = Wordle(word)

    while wordle.stillAttempt():
        attempt = input("\nType your guess: ").upper()
        if len(attempt) != wordle.WORD_LENGTH:
            print(colored(f"Word must be {wordle.WORD_LENGTH} characters long!", "red"), end="")
            continue
        if attempt not in word_set:
            print(colored(f"{attempt} is not a valid word!", "red"), end="")
            continue

        wordle.attempt(attempt)
        displayResult(wordle)

    if wordle.gameWin():
        print(colored("CORRECT. Congratulations!", "green"))
    else:
        print(colored(f"WRONG. The answer is {word}!", "red"))

def WordsDatabase():
    with open("src/words.txt", "r") as source, open('src/dictionary.txt', 'w') as destination:
        for word in source.readlines():
            if len(word) == 6:
                destination.write(word)
    print("All words loaded.")

if __name__ == "__main__":
    # WordsDatabase()
    main()
