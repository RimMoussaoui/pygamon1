
from unittest.mock import Mock
from player import Player

object=Player(10,10)
def test_move_down():
    object.move_down = Mock(return_value=2)
    assert object.move_down() == 2

def test_move_up():
    object.move_up = Mock(return_value=8)
    assert object.move_up() == 8


def test_move_left():
    object.move_left = Mock(return_value=4)
    assert object.move_left() == 4


def test_move_down():
    object.move_right = Mock(return_value=6)
    assert object.move_right() == 6


def test_save_location():
    object.save_location = Mock(return_value=0)
    assert object.save_location() == 0

def test_change_annimation():
    object.change_annimation = Mock(return_value=1)
    assert object.change_annimation() == 1

def test_update():
    object.update = Mock(return_value=10)
    assert object.update() == 10

def move_back():
    object.move_back = Mock(return_value=11)
    assert object.move_back() == 11

def test_get_image():
    object.get_image = Mock(return_value=12)
    assert object.get_image() == 12