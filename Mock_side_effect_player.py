from player import Player
from unittest.mock import Mock
import pygame

object=Player(10,10)
object.position = [10,10]

def test_move_right():
    def special_move_right():
        return object.position

    object.move_right = Mock()
    object.move_right.side_effect = special_move_right()
    assert object.move_right() == 10


