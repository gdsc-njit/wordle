class LetterState:
    def __init__(self, character: str):
        self.character = character
        self.in_word = False
        self.in_right_position = False
