
from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
            # The purpose of the setup phase is to prepare the objects or environment
            # needed for testing. Here, the object new_game is the key element
            # being prepared for the rest of the test.
            new_game = Game()

            # The exercise phase is where you "exercise" or invoke the functionality
            # being tested.
            grid = new_game.grid

            # verify
            #This checks that the grid is a list.
            assert isinstance(grid, list)

            #This ensures that the length of the grid is exactly 9, meaning it contains 9 elements. This suggests that the game requires a grid of 9 letters.
            assert len(grid) == 9
            for letter in grid:
                assert letter in string.ascii_uppercase #This ensures the grid only contains valid letters.

    def test_space_in_word(self):

        new_game = Game()
        test_word = 'ERH YUE'
        assert new_game.is_valid(test_word) is False

    def test_contained_in_grid(self):

        new_game = Game()
        test_word = 'VOIR'
        assert new_game.is_valid(test_word) is True

    def test_upper_case(self):
        new_game = Game()
        test_word = 'ertyh'
        assert new_game.is_valid(test_word) is False

    def test_unknown_word_is_invalid(self):
        """A word that is not in the English dictionary should not be valid"""
        new_game = Game()
        new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
        assert new_game.is_valid('FEUN') is False
