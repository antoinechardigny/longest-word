import requests

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = ['E','F','T','T','O','A','B','U','N']

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        bool_ = set(word).issubset(set(self.grid))
        if bool_:
            data = requests.get(f'https://dictionary.lewagon.com/{word}').json()
            is_valid = data['found']
        else:
            is_valid = False
        return is_valid

if __name__ == "__main__":
    game = Game()
    print(game.grid) # --> OQUWRBAZE
    my_word = 'TOMATO'
    print(game.is_valid(my_word)) # --> True
