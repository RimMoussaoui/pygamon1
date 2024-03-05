import unittest
import pygame
from game import Game
from player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.player = Player(self.game)

    def test_change_annimation(self):
        # Test with valid animation name
        self.player.change_annimation('up')
        self.assertEqual(self.player.image, self.player.images['up'])
        self.assertEqual(self.player.current_animation, 'up')

        # Test with invalid animation name
        with self.assertRaises(KeyError):
            self.player.change_annimation('invalid')

        # Test with None animation name
        with self.assertRaises(TypeError):
            self.player.change_annimation(None)

        # Test with empty animation name
        with self.assertRaises(KeyError):
            self.player.change_annimation('')

        # Test with no animation name
        self.player.change_annimation()
        self.assertIsNone(self.player.current_animation)

if __name__ == '__main__':
    unittest.main()