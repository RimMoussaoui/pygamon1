import unittest
import pygame
from game import Game
from player import Player

class TestHandelInput(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.player = Player(self.game)

    def test_move_up(self):
        self.game.input_manager.pressed_keys[pygame.K_UP] = True
        self.player.handel_input(self.game)
        self.assertEqual(self.player.rect.y, 0)
        self.assertEqual(self.player.current_animation, 'up')

    def test_move_down(self):
        self.game.input_manager.pressed_keys[pygame.K_DOWN] = True
        self.player.handel_input(self.game)
        self.assertEqual(self.player.rect.y, 0)
        self.assertEqual(self.player.current_animation, 'down')

    def test_move_left(self):
        self.game.input_manager.pressed_keys[pygame.K_LEFT] = True
        self.player.handel_input(self.game)
        self.assertEqual(self.player.rect.x, 0)
        self.assertEqual(self.player.current_animation, 'left')

    def test_move_right(self):
        self.game.input_manager.pressed_keys[pygame.K_RIGHT] = True
        self.player.handel_input(self.game)
        self.assertEqual(self.player.rect.x, 0)
        self.assertEqual(self.player.current_animation, 'right')

    def test_no_movement(self):
        self.player.handel_input(self.game)
        self.assertEqual(self.player.rect.x, 0)
        self.assertEqual(self.player.rect.y, 0)
        self.assertIsNone(self.player.current_animation)

if __name__ == '__main__':
    unittest.main()