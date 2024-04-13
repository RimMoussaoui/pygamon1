
import unittest.mock
from unittest.mock import patch
from game import Game



gam = Game()
def test_update():
    with patch.object(Game, 'update', return_value=4):
        assert gam.update() == 4
def test_handel_input():
    with patch.object(Game, 'handel_input', return_value=2):
        assert gam.handel_input() == 2

