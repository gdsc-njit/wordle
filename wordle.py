from letter_state import LetterState

class Wordle:
    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5
    VOIDED_LETTER = "*"

    def __init__(self, secret: str):
        self.secret = secret.upper()
        self.attempts = []

    def attempt(self, word: str):
        word = word.upper()
        self.attempts.append(word)

    def guess(self, word: str):
        word = word.upper()

        # Initialize the results array
        result = [LetterState(x) for x in word]

        # Convert a copy of secret to a list
        remaining_secret = list(self.secret)

        # check for GREEN letters
        for i in range(self.WORD_LENGTH):
            letter = result[i]
            if letter.character == remaining_secret[i]:
                letter.in_right_position = True
                remaining_secret[i] = self.VOIDED_LETTER

        # check for YELLOW letters
        for i in range(self.WORD_LENGTH):
            letter = result[i]

            # Skip letter if it is already in the right place
            if letter.in_right_position:
                continue

            # Otherwise, check if the letter is in the word, and void that index
            for j in range(self.WORD_LENGTH):
                if letter.character == remaining_secret[j]:
                    remaining_secret[j] = self.VOIDED_LETTER
                    letter.in_word = True
                    break
        return result

    def gameWin(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret
    
    def remainingAttempts(self): # integer
        return self.MAX_ATTEMPTS - len(self.attempts)

    def stillAttempt(self):
        return self.remainingAttempts() > 0 and not self.gameWin()
