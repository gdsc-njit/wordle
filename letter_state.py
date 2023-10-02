class LetterState:
    def __init__(self, character: str):
        self.character = character
        self.is_in_word = False
        self.is_in_position = False
