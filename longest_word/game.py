class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = ['G','R','E','Q','I','V','B','M','O']

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        bool_ = set(word).issubset(set(self.grid))
        return bool_

if __name__ == "__main__":
    game = Game()
    print(game.grid) # --> OQUWRBAZE
    my_word = 1000
    print(game.is_valid(my_word)) # --> True
